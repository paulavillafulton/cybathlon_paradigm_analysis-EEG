% clear all
% close all
% clc

calibration = pop_loadxdf('C:\Users\cybathlon\Desktop\Paradigm group\recorded_data\PA_corey2601.xdf');
%% data preprocessing
%y = pop_select(calibration, 'channel', [1:24]);
% y = pop_resample(y, 250);
% y = pop_rmbase(y,[],[]);
y = calibration
y = pop_eegfilt(y, 1, 0, 0, 0, 0, 0, 'fir1', 0);       % first highpass the data
y = pop_eegfilt(y, 0, 40, 0, 0, 0, 0, 'fir1', 0);      % then lowpass the data
% y = pop_reref(y,[]);

%% data epoching and resampling
all_events = pop_epoch(y,{'c','wi','wl'},[-0.5 1]);
error_blocks = pop_select(all_events, 'notrial', [1:360,481:540]);

EEG_epo_noError = pop_epoch(error_blocks,{'c'},[0 0.5]); % no-error epochs
EEG_epo_noError = pop_rmbase(EEG_epo_noError,[],[]);
EEG_epo_Error = pop_epoch(error_blocks,{'wl','wi'},[0 0.5]); % error epochs
EEG_epo_Error = pop_rmbase(EEG_epo_Error,[],[]);
EEG_epo_Error_Pos = pop_epoch(error_blocks,{'wl'},[0 0.5]); % error epochs location
EEG_epo_Error_Pos = pop_rmbase(EEG_epo_Error_Pos,[],[]);
EEG_epo_Error_Int = pop_epoch(error_blocks,{'wi'},[0 0.5]); % error epochs intensity
EEG_epo_Error_Int = pop_rmbase(EEG_epo_Error_Int,[],[]);

resamp_noError = pop_resample(EEG_epo_noError, 100);
% resamp_Error = pop_resample(EEG_epo_Error, 100);
resamp_ErrorPos = pop_resample(EEG_epo_Error_Pos, 100);
resamp_ErrorInt = pop_resample(EEG_epo_Error_Int, 100);

%% dimensionality reduction
% create feature matrices
feat_noError = reshape(resamp_noError.data(1,:,:),[],size(resamp_noError.data,3))';
% feat_Error = reshape(resamp_Error.data(3,:,:),[],size(resamp_Error.data,3))';
feat_ErrorPos = reshape(resamp_ErrorPos.data(1,:,:),[],size(resamp_ErrorPos.data,3))';
feat_ErrorInt = reshape(resamp_ErrorInt.data(1,:,:),[],size(resamp_ErrorInt.data,3))';

% put all features into one single array
all_feat = [feat_noError;feat_ErrorPos;feat_ErrorInt];

labels = [-1*ones(size(feat_noError,1),1);
          1*ones(size(feat_ErrorPos,1),1);
          2*ones(size(feat_ErrorInt,1),1)];
colors = [ones(sum(labels==-1),1)*[0, 0.4470, 0.7410],
          ones(sum(labels==1),1)*[0.8500, 0.3250, 0.0980],
          ones(sum(labels==2),1)*[0.9290, 0.6940, 0.1250]];
      
indices = crossvalind('Kfold',labels,10);
mcr = [];

for k=1:10
    test_idx = (indices==k);
    train_idx = ~test_idx;
    
    train_data = all_feat(train_idx,:);
    train_labels = labels(train_idx);
    test_data = all_feat(test_idx,:);
    test_labels = labels(test_idx);
    
    train_data_norm = normalize(train_data,1,'zscore'); % this is actually standardization;
    test_data_norm = normalize(test_data,1,'zscore'); % this is actually standardization;
    
    [train_pca, mapping_pca] = compute_mapping(train_data_norm, 'PCA', 10);
    test_pca = test_data_norm*mapping_pca.M;
    
    MdlQuadratic = fitcdiscr(train_pca,train_labels,'DiscrimType','quadratic');
    test_results = predict(MdlQuadratic,test_pca);
    mcr = [mcr,sum(test_results~=test_labels)/size(test_pca,1)]; 
end

MCR_mean = mean(mcr)
MCR_std = std(mcr)
      
% ind_perm = randperm(length(labels));
% labels = labels(ind_perm);
% colors = colors(ind_perm,:);

% [score, mapping] = compute_mapping([labels,score_pca], 'LDA', 2);
% figure;
% scatter(score(:,1),score(:,2),20,colors,'filled')
% % axis equal
% xlabel('1st Component')
% ylabel('2nd Component')
% title('LDA')