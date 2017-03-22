import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def rate(image):
    # Read in the image_data
    image_data = tf.gfile.FastGFile(image, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        # for node_id in top_k:
        node_id = top_k[0]
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        # print('%s (score = %.5f)' % (human_string, score))
        return human_string


if __name__ == '__main__':
    import sys
    from pyfiglet import Figlet

    image_path = sys.argv[1]
    f = Figlet(font='slant')

    print '\nthis poo looks like a...'
    rating = rate(image_path)
    print f.renderText(rating)
