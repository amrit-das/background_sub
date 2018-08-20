cv::Mat mat; // load img, etc

#include <opencv2/highgui.hpp>
#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>

int main() {
  
  cv::Mat mat;
  //cv::Mat gray;

cv::setMouseCallback("Test", my_mouse_callback, (void*) &mat);
// ...
void my_mouse_callback(int event, int x, int y, int flags, void* param){
cv::Mat mat = *((cv::Mat*)param);  // so, 1st cast, then deref
}
  
image = cv::imread("rgb_wheel.png" , CV_LOAD_IMAGE_COLOR);
 // cv::cvtColor(image,gray,cv::COLOR_BGR2GRAY);
  //cv::namedWindow( "Display window", cv::WINDOW_AUTOSIZE );
 cv::Mat img_rgb = cv::imread("rgb_wheel.png");
cv::imshow( "Display window", image );
 // cv::imshow("Gray Image",gray);
 cv::waitKey(0);
}

