import imageio.v3 as iio

#to store location of the images
filenames = ['team-pic1.png', 'team-pic2.png']

#to store actual image
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration=500, loop=0)