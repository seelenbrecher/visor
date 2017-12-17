# Installation
sudo apt-get update
sudo apt-get upgrade

Build tools:
sudo apt install build-essential cmake pkg-config

Image codecs:
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev

Video codecs:
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev

OpenCV GUI:
sudo apt-get install libgtk-3-dev

Matrix Ops optimization:
sudo apt-get install libatlas-base-dev gfortran

SUMMARY:
sudo apt install build-essential cmake pkg-config libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev libatlas-base-dev gfortran


wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip && unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip && unzip opencv_contrib.zip

Python Wrapper:
python3 -m venv env
source env/bin/activate
pip install numpy

cd opencv-3.3.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.3.0/modules \
    -D BUILD_EXAMPLES=ON ..

Finally:
make
sudo make install
sudo ldconfig

Symlink cv2 from /usr/local/lib/python2.7/site-packages/ to virtualenv location:
cd /usr/local/lib/python3.5/site-packages/
sudo mv cv2.cpython-35m-x86_64-linux-gnu.so cv2.so
ln -s /usr/local/lib/python3.5/site-packages/cv2.so <YOUR_VIRTUAL_ENV_FOLDER>/lib/python3.5/site-packages/cv2.so

Clean unused files:
cd <OBJECT_DETECTION_FOLDER>
rm -rf opencv-3.3.0/ opencv_contrib-3.3.0/ opencv_contrib.zip opencv.zip
