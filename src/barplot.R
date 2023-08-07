library(ggplot2)
library(wesanderson)
data <- read.csv(("F:/YAO_2023/Apple/workspace/data/barplot.csv"),header = T)
data$No..of.information.sources <- as.character(data$No..of.information.sources)
windowsFonts(A = windowsFont("Times New Roman"))
ggplot(data,mapping = aes(Production_stage,Count,fill=No..of.information.sources))+
  geom_bar(stat='identity',position='fill') +labs(x = 'Management decisions',y = 'Share of surveyed appler farmers',fill = "No. of information sources") +
  theme(axis.text.x = element_text(family = "A", angle = 45, hjust = 1))+ theme_bw() + 
  theme(panel.grid.major = element_blank(),panel.grid.minor = element_blank())+
  theme(axis.text = element_text(family = "A", size = 12),axis.title = element_text(family = "A", size = 14, color = 'black'),
        legend.title = element_text(family = "A", size = 12,color = 'black'),legend.text = element_text(family = "A", size=10))+
  theme(legend.position = "top")+
  scale_fill_manual(values = c( "1"="#33a02c", "2"="#377eb8", "3"="#984ea3", "4"="#d95f02", "5"="#e41a1c"))+
  coord_flip()

