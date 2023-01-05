## import the library
library(dplyr)

## read the data
df <- read.csv("/home/fireball/Desktop/database_intro/final project/skills_database.csv")

## distinct 
ndf <- distinct(df, Skills)

View(ndf)
ndf$Skills[1]

write.csv(ndf, "/home/fireball/Desktop/database_intro/final project/all_skills.csv", row.names = FALSE)
