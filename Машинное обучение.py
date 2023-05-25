from pixellib.instance import instance_segmentation


def object_detection_image():
    segment_image = instance_segmentation()
    segment_image.load_model('C:\Users\user\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\mask_rcnn_coco.h5')

    segment_image.segmentImage(
        image_path='ball1.jpg',
        output_image_name='ball2.jpg'

    )

def main():
    object_detection_image()

if __name__=='__main__':
    main()