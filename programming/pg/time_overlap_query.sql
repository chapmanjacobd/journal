SELECT e1.pk, e1.event, e2.*  
 FROM events e1, 
 LATERAL ( SELECT pk, event, ts - e1.ts as time_elapsed 
           FROM events 
           WHERE pk <> e1.pk AND e1.ts - ts <= '10 minutes'::interval ) e2 
ORDER BY e1.pk LIMIT 20;
