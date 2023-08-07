library(ggplot2)
library(wesanderson)
df=read.csv("D:/workspace/apple/Apple-survey.com/data/fao_data.csv")
ylabs <- expression(paste("Yield (",kg/ha,")"))
windowsFonts(myFont1 = windowsFont("Times New Roman"))
p0<-ggplot(data=df, aes(x=Year, y=Value, color=Country, shape=Country))+
  geom_point(size = 3.5)+geom_line(size = 1.5)+labs(x="",y=ylabs,family="myFont1")+ 
  theme_bw()+theme(panel.grid.major = element_blank(),panel.grid.minor = element_blank())+
  theme(axis.text = element_text(family="myFont1",size = 18),axis.title = element_text(family="myFont1",size = 18, color = 'black'),
        legend.title = element_text(size = 18, color = 'black'),legend.text = element_text(family="myFont1",size=20))+
  theme(axis.line = element_line(colour = "black"))+
  theme(axis.text.x = element_text(family="myFont1",angle = 30, hjust = 1, vjust = 1))+
  theme(legend.position = "top" )+
  scale_x_continuous(breaks = seq(1990,2020,2))+
  scale_y_continuous(breaks = seq(10000,60000,10000))

p1<-p0+scale_color_manual(values=c("#33a02c", "#0570b0", "#984ea3", "#f0027f", "#bf5b17"))

print(p1)
