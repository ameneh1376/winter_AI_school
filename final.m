digitDatasetPath = fullfile('datafinal');
imds = imageDatastore(digitDatasetPath, ...
    'IncludeSubfolders',true,'LabelSource','foldernames');
figure;
perm = randperm(100,20);
for i = 1:20
    subplot(4,5,i);
    imshow(imds.Files{perm(i)});
end
labelCount = countEachLabel(imds)
img = readimage(imds,1);
size(img)
trainNumFiles =900;
[trainDigitData,valDigitData] = splitEachLabel(imds,trainNumFiles,'randomize');
 layers = [
    
    imageInputLayer([4 5 1])

    convolution2dLayer(2,16,'Padding',1)
    
    reluLayer

    maxPooling2dLayer(2,'Stride',2)
    crossChannelNormalizationLayer(3);

    convolution2dLayer(2,32,'Padding',1)
    
    reluLayer
% 
%     maxPooling2dLayer(2,'Stride',2)
% 
%     convolution2dLayer([1 2],64,'Padding',1)
%     
%     reluLayer
crossChannelNormalizationLayer(3);

    fullyConnectedLayer(2)
    softmaxLayer
    classificationLayer];
options = trainingOptions('sgdm');

net = trainNetwork(trainDigitData,layers,options);
predictedLabels = classify(net,valDigitData);
valLabels = valDigitData.Labels;

accuracy = sum(predictedLabels == valLabels)/numel(valLabels)
