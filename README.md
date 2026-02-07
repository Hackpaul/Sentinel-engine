# Sentinel Engine 🛡️

**High-Performance IP Indexing Module for DDoS Detection**

A pure Python engine optimized for extreme throughput and low latency. It maps IPv4 addresses to hashed buckets using bitwise operations and prime modulo hashing, designed to track request frequency in real-time.

---

### 🚀 Performance Benchmarks
* **Throughput:** ~972,000 Requests Per Second (RPS)
* **Latency:** ~1.02 microseconds per packet
* **Environment:** Single-threaded Python 3.14 (Laptop CPU)

---

### ⚡ Core Algorithm
1.  **Compression:** Compresses 4-part IPv4 addresses into a 32-bit integer using **Bitwise Left Shift** (`<<`).
2.  **Hashing:** Maps the integer to a fixed bucket index using **Prime Modulo** (`% 1000003`).
3.  **Registration:** Tracks hit frequency using a direct-access array.

### 🔧 Optimization Techniques 
To achieve <1.1µs latency in pure Python, I utilized:
* **Loop Inlining:** Replaced function calls with inline bitwise logic to eliminate stack overhead.
* **Local Caching:** Cached global variables (`ip_mapper`, `prime`) to local scope to minimize lookup time.
* **Tuple Processing:** Switched from Lists to Tuples for faster memory access.
