There is so much misinformation online that the only way to learn is to be skeptical and Google things many times until you find the right answer. 

Even ESRI has some slightly incorrect algorithms. Because spatial autocorrelation is significant for things that are meaningful it usually doesn't matter that much for a final output calculation but if it is just one part in a larger system or an ML pipeline there might be some meaningful data which is blurred or misrepresented. So if you have a pipeline which is important it might make sense to invest time to audit each transformation to ensure validity and performance. GeoDa and PySAL are pretty solid in terms of implementing spatial statistics. WhiteboxTools is pretty solid for some transformations

TL;DR Try many tools, compare speed (and accuracy with a manual calculation). Most tools have one or more flaws.
