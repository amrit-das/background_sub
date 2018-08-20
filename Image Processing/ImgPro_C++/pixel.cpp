#include <opencv2/highgui.hpp>
#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
using namespace std;
using namespace cv;
int main() 
{
  
  cv::Mat image;
  //cv::Mat gray;
  image = cv::imread("rgb_wheel.png");
 // cv::cvtColor(image,gray,cv::COLOR_BGR2GRAY);
  //cv::namedWindow( "Display window", cv::WINDOW_AUTOSIZE );
// cv::Mat img_rgb = cv::imread("rgb_wheel.png");
for(int i = 0; i < image.rows; i++)
{
    for(int j = 0; j < image.cols; j++)
    {
        int b = image.at<cv::Vec3b>(i,j)[0];
        int g = image.at<cv::Vec3b>(i,j)[1];
        int r = image.at<cv::Vec3b>(i,j)[2];
        cout<<r<<" "<<g<<" "<<b<<endl;
    }
}
cv::imshow( "Display window", image );
  cv::waitKey(0);
}


//Point3_<uchar>* p = img_rgb.ptr<Point3_<uchar> >(10,10);
//p->x; //B
//p->y; //G
//p->z; //R
//std::cout<<p; 
 // cv::imshow("Gray Image",gray);
// std::cout<<p;  
