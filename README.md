"""
sentinel_engine - High performing IP Indexing Module.

Core Algorithm :

    1.compress IPv4_addresses to a 32-bit integer (Bit wise left shift).
    2.maps the integer to a bucket index using Prime modulo hashing.
    3.registers request Frequency to detect DDoS patterns .

    Measured Latency ~ 1078 ns (Benchmark)

