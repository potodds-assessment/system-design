# Data Consistency in a Distributed Architecture

**CAP theorem (Consistency, Availability, Partition Tolerance)**
- consistency: strong, eventual, causal
- data replication: primary-seconday, leaderless
- consensus algorithms: Paxos, Raft. Nodes agree on update ordering
- conflict resolution: last-write-wins, application specific conflict resolution
- ACID apps: 2 phase commit, Paxos commit
- data partitioning: hash, range
- caching: cache invalidation, cache update
- monitor/detect inconsistencies
- design for failure: fail gracefully to prevent data corruption
- appropriate database: SQL, NoSQL, distributed


**Caching consistency solutions**
---
*Write-through cache*  
updates written to both cache and database simultaneously

*Write-back caching*  
In write-back caching, updates are initially written to the cache and then asynchronously propagated to the underlying data store. This improves write performance but introduces a risk of inconsistency if the cache fails before updates are synchronized.

*Cache invalidation*  
Cache invalidation mechanisms proactively remove stale data from the cache to ensure consistency. This can be done through time-based expiration, event-based invalidation, or explicit cache eviction.

*Cache consistency protocols*  
Cache consistency protocols like Memcached's Memcache Binary Protocol (MCBP) or HTTP-based cache invalidation headers help maintain consistency across distributed caches.

*Versioning*  
Versioning schemes assign unique identifiers to data items, allowing caches to detect and handle stale data. Optimistic locking and conditional requests can be used to prevent conflicts.

*Read-through caching*  
In read-through caching, data is only loaded into the cache when it is requested. This ensures that the cache always holds the latest data from the data store.

*Write-around caching*  
In write-around caching, updates bypass the cache and are written directly to the data store. This is useful for frequently updated data where caching is less beneficial.

*Eventual consistency*  
Eventual consistency allows temporary inconsistencies but guarantees that all replicas will eventually converge to the same state. This is suitable for applications that can tolerate some inconsistency for improved performance.

*Strong consistency*  
Strong consistency ensures that all reads always return the latest written value. This is achieved through mechanisms like consensus algorithms or distributed transactions.

*Data partitioning*  
Partitioning data across multiple caches can reduce contention and improve scalability. However, it introduces the challenge of maintaining consistency across partitions.

*Conflict resolution*  
When conflicts arise due to concurrent updates, conflict resolution strategies like last-write-wins or application-specific logic can be employed.
