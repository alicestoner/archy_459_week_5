library(readxl)
library(dplyr)
library(tidyr)

tww <- read_excel("data/CNN-Models-Supplement/TWW_data.xlsx")

type_levels <- c("Kanaa", "Wepo", "Black_Mesa", "Sosi", "Dogoszhi", "Flagstaff", "Tusayan", "Kayenta")

# Create sherds like in the QMD
sherds <- tww |> 
  transmute(
    image = image_file,
    type = factor(`Human consensus`, levels = type_levels),
    paper_prediction = `CNN model prediction`
  )

# Create confusion matrix between type (actual) and paper_prediction (predicted)
confusion <- sherds |> 
  count(type, paper_prediction) |> 
  complete(type, paper_prediction, fill = list(n = 0)) |> 
  arrange(desc(n))

cat("Confusion matrix (actual type vs CNN model prediction), arranged by count (descending):\n")
print(confusion)

cat("\nTop 10 most confused pairs:\n")
head(confusion, 10) |> 
  mutate(pair = paste(type, paper_prediction, sep="->")) |> 
  pull(pair) |> 
  cat(sep="\n")

cat("\nAre the most confused types neighbors in the ordering?\n")
# The type ordering: Kanaa, Wepo, Black_Mesa, Sosi, Dogoszhi, Flagstaff, Tusayan, Kayenta
order <- c("Kanaa"=1, "Wepo"=2, "Black_Mesa"=3, "Sosi"=4, "Dogoszhi"=5, "Flagstaff"=6, "Tusayan"=7, "Kayenta"=8)

for (i in 1:nrow(head(confusion, 10))) {
  row <- head(confusion, 10)[i, ]
  type_idx <- order[row$type]
  pred_idx <- order[row$paper_prediction]
  is_adjacent <- abs(type_idx - pred_idx) == 1
  cat(sprintf("%s <-> %s: positions %d, %d, adjacent=%s, n=%d\n",
              row$type, row$paper_prediction, type_idx, pred_idx, is_adjacent, row$n))
}