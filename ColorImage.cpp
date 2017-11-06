
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"

 // Author Rishab Shah

using namespace cv;
using namespace std;
 
int main(int argc, char** argv )
{
    Mat src;
    src = imread(argv[1], CV_LOAD_IMAGE_COLOR);
    namedWindow( "Original image", CV_WINDOW_AUTOSIZE );
    imshow( "Original image", src); // THIS IS DISPLAYING THE ORIGINAL COLOURED IMAGE OF THE LADY.

	vector<Mat> input_planes(3);
	split(src,input_planes);
	Mat channel1_display, channel2_display, channel3_display;
	// IT IS USING BGR FORMAT HERE(3 CHANNELS)
	// HERE ALL THE 3 CHANNELS ARE BEING DISPLAYED INDIVIDUALLY
        imshow("Red",   input_planes[2]); //RED CHANNEL
        imshow("Green",   input_planes[1]); // GREEN CHANNEL
        imshow("Blue",   input_planes[0]); // BLUE CHANNEL


	Mat ycrcb_image;
	// THIS IS THE YCbCr FORMAT WHICH ALSO HAS 3 CHANNELS , Y - LUMA COMPONENT, Cb - BLUE DIFFERENCE , Cr - RED DIFFERENCE 
	// AGAIN THE INDIVIDUAL CHANNELS ARE DISPALYED
	cvtColor(src, ycrcb_image, CV_BGR2YCrCb); // THIS CONVERTS THE IMAGE TO YCrCb format
	split(ycrcb_image,input_planes);
        imshow("Y",   input_planes[0]); // Y CHANNEL
        imshow("Cb",   input_planes[1]); // Cb CHANNEL
        imshow("Cr",   input_planes[2]); // Cr CHANNEL


	Mat hsv_image;
	cvtColor(src, hsv_image, CV_BGR2HSV);// THIS CONVERTS THE IMAGE TO HSV format
	vector<Mat> hsv_planes(3);
	// HSV - HUE , SATURATION , VALUE
	split(hsv_image,hsv_planes);
        imshow("Hue",   hsv_planes[0]); // H CHANNEL
        imshow("Saturation",   hsv_planes[1]); // SATURATION  CHANNEL
        imshow("Value",   hsv_planes[2]); // VALUE CHANNEL 


	
    waitKey(0); // THIS SUGGESTS THAT THE IMAGE SHOULD BE VISIBLE TILL A USER DOESNT CLICK ANY KEY.                                      
    return 0;
} 

