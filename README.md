# GeoNamesEmbedding
Word2Vec embedding of place names and geographic terms.

I initially created this in August, 2019, for use on GeoGenius, a geography portal I co-founded. However, it proved unessecary for the task at hand so I have not touched it since then. It was able to create some impressive embeddings however so I'm pushing it to Github.

The training set consists of thousands of geography factfiles and questions that were synthesized into models using Word2Vec from Gensim, and some of the models have created some truly impressive connections, in my opinion. Some of the materials in the set are private and have been used with their owners' permission so the training materials are not commited publically to this repo, though if anybody wants access to these materials feel free to contact me about it.

All the models are in (surprise) the models folder, and models are grouped into corpus versions, currently 1-7, with each corpus reflecting material that was added to the training set. The best models tend to be from the latest corpus versions, which is currently number 7.
