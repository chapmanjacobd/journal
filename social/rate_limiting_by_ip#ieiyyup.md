If applicable, you might also try reusing some computation via caching

  


    from cachetools import func
    @func.ttl_cache(maxsize=50_000, ttl=THREE_DAYS)
