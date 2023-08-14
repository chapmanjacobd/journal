nc = nc[order(nc$COUNTY),]
adj = st_touches(nc, sparse=FALSE)
str(adj)
## logi [1:100, 1:100] FALSE FALSE FALSE FALSE FALSE FALSE ...
durham = which(nc$COUNTY == "Durham County")
nc %>% slice(which(adj[durham,])) %>% .$COUNTY
## [1] "Chatham County" "Granville County" "Orange County"
## [4] "Person County" "Wake County"
library(corrplot)
rownames(adj) = str_replace(nc$COUNTY, ” County”, ””)
colnames(adj) = str_replace(nc$COUNTY, ” County”, ””)
corrplot(adj[1:20,1:20],method=”color”,type=”full”,tl.col=”black”,cl.pos = ”

most_neighbors = rowSums(adj)==max(rowSums(adj))
plot(st_geometry(nc))
plot(st_geometry(nc[most_neighbors,]),add=TRUE,col=”lightblue”)

nc$COUNTY[most_neighbors]


least_neighbors = rowSums(adj)==min(rowSums(adj))
plot(st_geometry(nc))
plot(st_geometry(nc[least_neighbors,]),add=TRUE,col=”lightblue”)

nc$COUNTY[least_neighbors]
