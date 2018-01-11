information <- read.csv("IraqIS.csv")

#For the beginning, I want to compare 2004 to 2016
iraq04.16 <- information %>%
  filter(year %in% c(2004, 2016)) %>%
  droplevels()
iraq04.16

#I plot two bar graphs that show the difference of fatalities and civilian deaths from 2004 and 2016 
ggplot(data = iraq04.16) + geom_col(mapping = aes(x = year, y = fatalities), width = 1)
ggplot(data = iraq04.16) + geom_col(mapping = aes(x = year, y = deaths_civilians), width = 1)

#In a last step I want to see the development over the time the IS has been active in Iraq
ggplot(data = information) + geom_line(mapping = aes(x = year, y = fatalities))
ggplot(data = information) + geom_line(mapping = aes(x = year, y = deaths_civilians))