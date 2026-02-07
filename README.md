sentinel_engine - High performing IP Indexing Module.



#Core Algorithm :

    1.compress IPv4_addresses to a 32-bit integer (Bit wise left shift).
    2.maps the integer to a bucket index using Prime modulo hashing.
    3.registers request Frequency to detect DDoS patterns .

    Measured Latency ~ 1078 ns (Benchmark)

 

#Optimized the core engine loop for maximum throughput:

   1. Replaced function calls with direct bitwise logic (Inlining) to remove stack overhead.
   2. Cached global variables (ip_mapper, prime) to local scope to reduce lookup time.
   3. Result: Latency reduced to ~1.02 microseconds per packet.

    Measured RPM : ~ 970k Request per Second  
