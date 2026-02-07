

"""
sentinel_engine - High performing IP Indexing Module.

Core Algorithm :

    1.compress IPv4_addresses to a 32-bit integer (Bit wise left shift).
    2.maps the integer to a bucket index using Prime modulo hashing.
    3.registers request Frequency to detect DDoS patterns .

    Measured Latency ~ 1078 ns (Benchmark)

"""


from time import perf_counter_ns

ip_mapper=[0]*1000003 #the map of the ip_addresses
prime_number=1000003 #the prime number used to modulus the index to distribute even patterns

def ip_address_to_hashed_index(register,ip_address,prime) :
    ip_index=(ip_address[0]<<24)+(ip_address[1]<<16)+(ip_address[2]<<8)+(ip_address[3])
    ip_index=ip_index % prime
    register[ip_index]+=1

# a test loop only runs on main .
if __name__== "__main__":

    total_time,count=0,0

    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for h in range(0, 10):
                    ip_address_for_passing = [i, j, k, h]

                    t_1 = perf_counter_ns()
                    ip_address_to_hashed_index(ip_mapper, ip_address_for_passing, prime_number)
                    t_2 = perf_counter_ns()

                    total_time+=t_2 - t_1

                    count+=1

    average_time=total_time/count
    print("average latency:",average_time,"ns")






