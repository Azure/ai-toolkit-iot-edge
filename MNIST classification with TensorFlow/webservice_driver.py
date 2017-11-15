def init():
    import tensorflow as tf
    global sess, predict, x, keep_prob

    # load the saved tensorflow model and parameters
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.import_meta_graph('./my_ConvNet_MNIST_model.meta')
    saver.restore(sess,tf.train.latest_checkpoint('./'))
    graph = tf.get_default_graph()
    predict = graph.get_tensor_by_name("predout:0")
    x = graph.get_tensor_by_name("inputimage:0")
    keep_prob = graph.get_tensor_by_name("dropout:0")

def run(reqStr):
    import base64
    import json
    from PIL import Image
    from io import BytesIO
    from skimage.color import rgb2gray
    import numpy

    # decode the image
    images = json.loads(reqStr)
    base64ImgString = images[0]
    if base64ImgString.startswith('b\''):
        base64ImgString = base64ImgString[2:-1]
    base64Img = base64ImgString.encode('utf-8')
    decoded_img = base64.b64decode(base64Img)
    img_buffer = BytesIO(decoded_img)
    imageData = numpy.array(Image.open(img_buffer), dtype=numpy.float32)

    # convert the RGB array into grey-level
    imageData = imageData/255.0
    im = rgb2gray(imageData)
    im = im.reshape((1,im.shape[0]*im.shape[1]))
    im = list(im[0])
    
    # feed the image into the tensorflow model
    ims = [im]
    feed_dict = {x:ims, keep_prob:1.0}
    output = sess.run(predict,feed_dict)
    return(str(output[0]))