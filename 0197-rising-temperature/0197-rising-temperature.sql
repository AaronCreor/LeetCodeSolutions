select w.Id from  Weather w
join Weather w2 on w.recordDate = w2.recordDate+1
and w.temperature > w2.temperature