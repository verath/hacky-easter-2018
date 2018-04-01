import os
import shutil
import tensorflow as tf

import constants

SCRIPT_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(SCRIPT_DIR, 'model')

"""
"sp00n","n4m3","t41l","w31ght","c0l0r","ag3","l3ngth","g3nd3r","g00d"
11,"Daniel",11,2,"red",1,41,"male",False
"""
_CSV_COLUMNS = ['sp00n','n4m3','t41l','w31ght','c0l0r','ag3','l3ngth','g3nd3r','g00d']
_CSV_COLUMN_DEFAULTS = [[0], [''], [0], [0], [''], [0], [0], [''], [0]]


def build_estimator(model_dir):
    spoon = tf.feature_column.numeric_column('sp00n')
    name = tf.feature_column.categorical_column_with_hash_bucket('n4m3', hash_bucket_size=10000)
    tail = tf.feature_column.numeric_column('t41l')
    weight = tf.feature_column.numeric_column('w31ght')
    color = tf.feature_column.categorical_column_with_hash_bucket('c0l0r', hash_bucket_size=100)
    age = tf.feature_column.numeric_column('ag3')
    length = tf.feature_column.numeric_column('l3ngth')
    gender = tf.feature_column.categorical_column_with_vocabulary_list(
        'g3nd3r', ['female', 'male'])
    
    base_columns = [spoon, name, tail, weight, color, age, length, gender]

    return tf.estimator.LinearClassifier(
        model_dir=model_dir,
        feature_columns=base_columns)


def input_fn(data_file, num_epochs, shuffle, batch_size):
  assert tf.gfile.Exists(data_file)

  def parse_csv(value):
    print('Parsing', data_file)
    columns = tf.decode_csv(value, record_defaults=_CSV_COLUMN_DEFAULTS)
    features = dict(zip(_CSV_COLUMNS, columns))
    labels = features.pop('g00d')
    return features, tf.equal(labels, 1)

  # Extract lines from input files using the Dataset API.
  dataset = tf.data.TextLineDataset(data_file)
  dataset = dataset.skip(1) # skip header row  

  if shuffle:
    dataset = dataset.shuffle(buffer_size=10000)

  dataset = dataset.map(parse_csv, num_parallel_calls=5)
  dataset = dataset.repeat(num_epochs)
  dataset = dataset.batch(batch_size)
  return dataset


def main():
  # Clean up the model directory if present
  shutil.rmtree(MODEL_DIR, ignore_errors=True)
  model = build_estimator(MODEL_DIR)

  train_file = os.path.join(SCRIPT_DIR, 'data_train.csv')
  test_file = os.path.join(SCRIPT_DIR, 'data_test.csv')

  epochs_between_evals = 2
  batch_size = 40
  train_epochs = 40

  def train_input_fn():
    return input_fn(train_file, epochs_between_evals, True, batch_size)

  def eval_input_fn():
    return input_fn(test_file, 1, False, batch_size)

  # Train and evaluate the model every `epochs_between_evals` epochs.
  for n in range(train_epochs // epochs_between_evals):
    model.train(input_fn=train_input_fn)
    results = model.evaluate(input_fn=eval_input_fn)

    # Display evaluation metrics
    print('Results at epoch', (n + 1) * epochs_between_evals)
    print('-' * 60)

    for key in sorted(results):
      print('%s: %s' % (key, results[key]))


if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  main()
