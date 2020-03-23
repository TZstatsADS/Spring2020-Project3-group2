#############################################################
### Construct features and responses for training images  ###
#############################################################

feature_euclidean <- function(input_list = fiducial_pt_list, index){

  ### Step 3: Apply function in Step 2 to selected index of input list, output: a feature matrix with ncol = n(n-1) = 78*77 = 6006
  pairwise_dist_feature <- t(sapply(input_list[index], dist))%>%round(2)
  dim(pairwise_dist_feature) 
  
  ### Step 4: construct a dataframe containing features and label with nrow = length of index
  ### column bind feature matrix in Step 3 and corresponding features
  pairwise_data <- cbind(pairwise_dist_feature, info$emotion_idx[index])
  ### add column names
  colnames(pairwise_data) <- c(paste("feature", 1:(ncol(pairwise_data)-1), sep = ""), "emotion_idx")
  ### convert matrix to data frame
  pairwise_data <- as.data.frame(pairwise_data)
  ### convert label column to factor
  pairwise_data$emotion_idx <- as.factor(pairwise_data$emotion_idx)
  
  return(feature_df = pairwise_data)
}
