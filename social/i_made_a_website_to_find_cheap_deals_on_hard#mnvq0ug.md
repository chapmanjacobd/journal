hmm sorry. In the eBay API docs it says:

    eBay India (ebay.in) 
    Note: eBay India is no longer a functioning eBay marketplace

https://developer.ebay.com/api-docs/commerce/taxonomy/types/bas:MarketplaceIdEnum

https://ebay.in/ redirects to https://export.ebay.com/in/ seems like a similar export-oriented situation to https://www.ebay.com.tw/

### For shipping to India

Do you usually use the ebay.com marketplace and set the shipping to India? If so the [United States marketplace](https://unli.xyz/diskprices/us/) will be the most similar inventory.

**But I concede this is not an optimal experience**--the shipping price estimation won't be very precise though it should still be _proportionally_ accurate (sellers that overcharge on shipping will tend to overcharge regardless of the destination). It may help to limit the "Item Location" field to any South Asia countries.

Unfortunately, the eBay API data does not provide me with an easy way to provide you with a way to hide any listings/sellers which don't ship to India.

### For shipping from India

There's nothing in my code that prevents India listings from showing up except that the price of the item + the shipping estimation may not be low enough to show up. Also, if the seller/listing restricts shipping to the country of the eBay marketplace then it also won't show up :( If you have a specific example where you think something is wrong that would be helpful!
