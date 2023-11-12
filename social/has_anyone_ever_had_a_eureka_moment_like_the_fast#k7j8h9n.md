> deliberately unoptimized

I'm not saying things are completely un-optimized but that many things are under-optimized. Usually the reasons for this is compatibility with existing operating systems and user software.

I agree that most big companies are able to better utilize hardware although outside of large, specific systems like AWS S3 they usually solve this problem of under-utilization by running many containers or VMs on the same machine--which is fine, I have no qualms about that. My point above is mostly about PCs, desktop software, and end-user programming.

Some programs, especially AAA games, are very optimized in this regard. But most desktop software does not tackle the data queuing/loading problem as a separate challenge from CPU/RAM related problems. 

In many cases it doesn't matter whether IO is done by synchronous calls or by something like io_uring. It matters more that the program is designed to load before things are needed so that IO utilization is more constant. If there are cases where IO can be done early, similar to [CPU/RAM cache misses](https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html), many programs can benefit from this lower latency.

Yes, there are a few programs which utilize IO well but there are also many, many programs that don't. Batching and multi-processing (eg. GNU Parallel) is an acceptable solution here but few end-users know how to do that--or an interface isn't provided to be able to do that.

My main point in all this is that CPU+RAM is often optimized better from a programming language or compiler point of view but the largest gap that I currently see is IO and everything between the user and RAM. For example, most programs are using state of the art array sorting algorithms but the programmer often doesn't even start to think about IO as a problem to be solved.
