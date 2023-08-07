library("forestplot")
library("grid")
library("magrittr")
library("checkmate")
forest_data<-read.csv(("F:/YAO_2023/Apple/workspace/data/Forest_ST.csv"),header=T)
#head(forest_data)
#View(forest_data)
windowsFonts(A = windowsFont("Times New Roman"))
forestplot(as.matrix(forest_data[,1:4]),mean=forest_data$OR,lower=forest_data$lower,upper=forest_data$upper,
           is.summary=c(T,F,F,F,F,F,F,F),
           zero=1,boxsize=0.15,lineheight=unit(12,'mm'),
           lwd.zero=2,lwd.ci=2.5,xlab="Odds Ratio",lwd.xaxis=2.8,grid=TRUE,
           align="c",graphwidth=unit(60,"mm"),
           col=fpColors(box="black",lines="black",zero="black",axes = "black"),
           txt_gp=fpTxtGp(label = gpar(fontfamily = "A"),ticks = gpar(fontfamily = "A",cex=1.2),xlab=gpar(fontfamily = "A",cex=1.2),title=gpar(fontfamily = "A"),cex=1.2),
           hrzl_lines=list("1"=gpar(lwd=2,lty=1),"2"=gpar(lwd=2,lty=1),"9"=gpar(lwd=2,columns=1:5,col="#000044")),
           #title="The role of information source on technology adoption",
           graph.pos=4,
           ci.vertices=TRUE,ci.vertices.height = 0.08,xticks=c(0,1,2,3,4,5,6,7,8,9))

