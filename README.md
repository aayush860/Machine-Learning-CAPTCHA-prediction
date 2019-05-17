# Machine-Learning-CAPTCHA-prediction

This project use folloing steps to be complete->
1. Collection of MNIST images for various images
2. Using image processing to threshold image, using morphological transformation to dialate and erode images, then using various edge detection like(Canny, laplacian) and in the end countouring to seperate each letter form CAPTCHA.
3. After CAPTCHA seperation each letter is conerted to binary for further processing.
4. Now we train the machine learning model using the data provided.
5. While this process i tried many ML algo for the seperation (almost 8) but the best suited was SVM.
6. After Training was sucessfully completed i saved the model using joblib to use it in a faster way so that while predicting CAPTCHA it would be feasible to read and predict the CAPTCHA.
7. So i integrated the model with a selenium code i was writing to collect data. But the problem being CAPTCHA.(Now being solved by the svm model i trained)
8. So after collecting data most important part was to visialize data the the best way to do it using pyython's matplotlib library!
