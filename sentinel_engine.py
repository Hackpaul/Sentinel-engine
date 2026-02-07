

"""
sentinel_engine - High performing IP Indexing Module.

Core Algorithm :

    1.compress IPv4_addresses to a 32-bit integer (Bit wise left shift).
    2.maps the integer to a bucket index using Prime modulo hashing.
    3.registers request Frequency to detect DDoS patterns .

    Measured Latency ~ 1078 ns (Benchmark)

"""

""" 
the original core engine .

def ip_address_to_hashed_index(register,ip_address,prime) :
    ip_index=((ip_address[0]<<24)+(ip_address[1]<<16)+(ip_address[2]<<8)+(ip_address[3]))% prime
    register[ip_index]+=1
    
"""
import random
import time


ip_mapper=[0]*1000003 #the map of the ip_addresses
prime_number=1000003 #the prime number used to modulus the index to distribute even patterns


# a test loop only runs on main .
if __name__== "__main__":

    Total_fake_ips=100000
    mapper = ip_mapper
    total_time,count,ip_address_for_passing=0,0,[[0,0,0,0]*Total_fake_ips]

    print("Initialising... ")

    for i in range(Total_fake_ips):

        ip=[random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        ip_address_for_passing.append(ip)

    print("Fake ips generated ....")
    print("Starting engine..3..2..1;")

    t_1 = time.perf_counter()
    """ 
    --------------------------------------------------------------------------------------------------------
    A High speed optimisation : Inlining & Local Caching
    --------------------------------------------------------------------------------------------------------
    
    # I initially Changed  Function calls --> Inline function || Global Variable --> Local variable , to bypass
    python's function overhead.
    # This improves speed from ~600k RPS to ~970k RPS.
    
    
    ---------------------------------------------------------------------------------------------------------
    """

    for ip_address in ip_address_for_passing:
        ip_index = ((ip_address[0] << 24) + (ip_address[1] << 16) + (ip_address[2] << 8) + (ip_address[3]))% 1000003

        mapper[ip_index] += 1


    t_2 = time.perf_counter()
    total_time=t_2 - t_1

    duration=Total_fake_ips/total_time
    print("average latency:",duration,"packets per second")
    print("latency per packet :",total_time/Total_fake_ips)







