#include "cnpy.h"
#include <iostream>
#include <random>
#include <vector>

int main() {
    const size_t WIDTH = 100;
    const size_t HEIGHT = 100;
    const size_t NUM_MATRICES = 5;
    const size_t MATRIX_SIZE = WIDTH * HEIGHT;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dis(0.0f, 1.0f);

    // Generate and save individual .npy files
    for (size_t i = 0; i < NUM_MATRICES; i++) {
        std::vector<float> data(MATRIX_SIZE);
        for (size_t j = 0; j < MATRIX_SIZE; j++) {
            data[j] = dis(gen);
        }

        std::string filename = "matrix_" + std::to_string(i) + ".npy";
        std::vector<size_t> shape = {HEIGHT, WIDTH};
        cnpy::npy_save(filename, &data[0], shape);
        std::cout << "Saved " << filename << "\n";
    }

    // Generate and save as .npz with all matrices
    std::string npz_filename = "matrices.npz";
    for (size_t i = 0; i < NUM_MATRICES; i++) {
        std::vector<float> data(MATRIX_SIZE);
        for (size_t j = 0; j < MATRIX_SIZE; j++) {
            data[j] = dis(gen);
        }

        std::string varname = "matrix_" + std::to_string(i);
        std::vector<size_t> shape   = {HEIGHT, WIDTH};
        std::string         mode    = (i == 0) ? "w" : "a";
        cnpy::npz_save(npz_filename, varname, &data[0], shape, mode);
    }
    std::cout << "Saved " << npz_filename << "\n";

    std::cout << "\nGenerated 5 matrices (100x100 float32) in both .npy and .npz formats\n";
    return 0;
}
