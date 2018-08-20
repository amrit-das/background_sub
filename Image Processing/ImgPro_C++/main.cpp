#include <opencv2/highgui.hpp>
#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>

int main() {
  
  cv::Mat image;

  image = cv::imread("rgb_wheel.png");

  cv::imshow( "Display window", image );
  
  cv::waitKey(0);
}

