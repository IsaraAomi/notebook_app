#include <iostream>
#include <string>
#include <opencv2/opencv.hpp>

void convertToGrayscaleWithBrightness(const std::string& inputFilePath, const std::string& outputFilePath, int brightness) {
    cv::Mat image = cv::imread(inputFilePath, cv::IMREAD_GRAYSCALE);
    image += brightness;
    cv::imwrite(outputFilePath, image);
    std::cout << "Conversion complete: " << outputFilePath << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        std::cerr << "Usage: " << argv[0] << " <inputFilePath> <outputFilePath> <brightness>" << std::endl;
        return 1;
    }
    std::string inputFilePath = argv[1];
    std::string outputFilePath = argv[2];
    int brightness = std::stoi(argv[3]);
    convertToGrayscaleWithBrightness(inputFilePath, outputFilePath, brightness);
    return 0;
}
