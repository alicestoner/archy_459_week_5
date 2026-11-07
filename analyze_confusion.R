library(readxl)
tww <- read_excel("data/CNN-Models-Supplement/TWW_data.xlsx")

cat("Column names:\n")
cat(paste(names(tww), collapse="\n"), "\n\n")

cat("Human consensus distribution:\n")
print(table(tww$`Human consensus`))

cat("\nCNN model prediction distribution:\n")
print(table(tww$`CNN model prediction`))