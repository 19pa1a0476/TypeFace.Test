%%Load Image
image       = imread ('testimage.png')
image       = im2bw (image, 0.01)

%%Create Bounding Boxes
image       = bwlabel (image)
Properties  = regionprops (image, 'BoundingBox')

NumberOfBoxes = max(size(Properties))

figure; 
imshow (image)

for k   = 1:NumberOfBoxes
    Box = Properties(k).BoundingBox;
    rectangle('Position', [Box(1), Box(2), Box(3), Box(4),],...
        'EdgeColor', 'r', 'LineWidth', 2)
end