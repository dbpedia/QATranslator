# QATranslator

This experimentation was done as follows,

1. Dataset Creation using QALD datasets.
2. Train and evaluate the initial dataset on Tensorflow Neural Machine translation with attention [model](https://www.blogger.com/u/1/blog/post/edit/7948183821104122808/789201015065518066#).
3. Using [DBpedia Spotlight](https://www.blogger.com/u/1/blog/post/edit/7948183821104122808/789201015065518066#) to annotate the entities and create templates.
4. Manually evaluate the entity recognition process.
5. Train and evaluate the correctly annotated text on Tensorflow Neural Machine translation with attention [model](https://www.blogger.com/u/1/blog/post/edit/7948183821104122808/789201015065518066#).

### **1. Dataset Creation using QALD datasets.**

From the QALD datasets from QALD-3 to QALD-7, I created a dataset which consists of language pairs such as English-Spanish, English-Deutsch, etc. These pairs are created for all languages Deutsch, Spanish, French Brazilian Portuguese, Portuguese, Italian, Dutch, Hindi, Romanian, Persian, and Russian.

### **2. Train and evaluate the initial dataset on Tensorflow Neural Machine translation with attention model.**

Using the &quot;Tensorflow Neural Machine translation with attention model&quot;, trained the initial datasets created as said above and got the following results,

| **language** | **accuracy %** | **train set size** | **test set size** | **error %** | **wrong translation %** |
| --- | --- | --- | --- | --- | --- |
| Spanish | 60.6299 | 513 | 381 | 17 | 22 |
| German | 65.8595 | 563 | 413 | 12 | 21 |
| French | 63.3587 | 557 | 393 | 13 | 23 |
| Russian | 14.6666 | 399 | 150 | 74 | 11 |
| Italian | 31.6301 | 563 | 411 | 12 | 55 |
| Portuguese | 3.33333 | 399 | 150 | 74 | 22 |
| Portuguese\_BR | 4.54545 | 217 | 22 | 0 | 95 |
| Hindi | 37.3333 | 447 | 150 | 55 | 7 |
| Dutch | 61.9422 | 513 | 381 | 17 | 20 |
| Persian | 8.14479 | 567 | 221 | 32 | 59 |
| Romanian | 52.3026 | 534 | 159 | 21 | 25 |

After analyzing the results, I observed that the model failed to identify some words because they are not in its vocabulary. Most of the words are different entities such as CPU, Brooklyn bridge, etc.

### **3. Using DBpedia Spotlight to annotate the entities and create templates.**

For this experiment, I used the English-Spanish language pair dataset. Creating templates included these steps,

1. Annotate Text
2. Get Resource and Entity
3. Replace the Entity

For this task, we used [DBpedia Spotlight](https://www.blogger.com/u/1/blog/post/edit/7948183821104122808/789201015065518066#), which is a tool for annotating mentions of DBpedia resources in text, which helps to link information to the Linked Open Data cloud through DBpedia.

1. **Annotate Text**

Using the provided API from DBpedia Spotlight, the English sentences are annotated. By sending a request to &#39;/annotate&#39; endpoint the entities were annotated. Spotlight offers a parameter &quot;confidence&quot; to adjust the sensitivity of identifying an entity. I observed that using 0.2,0.3 confidence caused annotating non-entity words such as &quot;when&quot;, &quot;give&quot; etc. Therefore the confidence 0.5 is used for optimal performance. I observed that in that confidence level, the tool fails to identify some entities.

#### **2. Get Resouce and Entity**

As in the previous step the text is annotated, from the response given by Spotlight, I extracted the DBpedia resource and the entity. For example, if the annotated entity was &quot;New York&quot; the resource would be &quot;http://dbpedia.org/resource/New\_York&quot;.

#### **3. Replace the Entity**

The expectation of this step was to get a result as follow,

**1)** Which river does the Brooklyn Bridge cross? ==> Which river does the <entity> cross?

¿Por qué río cruza la Brooklyn Bridge? ==> ¿Por qué río cruza la <entidad>?

**2)** How many rivers and lakes are in South Carolina? ==> How many rivers and lakes are in <entity>?

¿Cuántos ríos y lagos hay en Carolina del Sur? ==> ¿Cuántos ríos y lagos hay en <entidad>?

For the 1) example shown above, the entity is &quot;Brooklyn Bridge&quot; which was annotated in the English text. The entity appears on the Spanish text as the same, therefore it can be replaced easily.

But in the 2) example the entity is different in Spanish text. For identifying the correct translation of the entity and replacing it, I used DBpedia SPARQL queries.

query = select ?label where {<http://dbpedia.org/resource/South_Carolina> rdfs:label ?label. filter(lang(?label) = 'es')}

Which returns the Spanish translation of the entity &quot;Carolina del Sur&quot;. Using this result the entity is replaced in the Spanish text. This process is done for all the text pairs. Finally, the template dataset is created by replacing the entities.

### **4.**  **Manually evaluate the entity recognition process.**

We used the resource returned by DBpedia spotlight to annotate the target language text. Since there were some resources not identified correctly, the annotation process was flawed. Therefore I had to manually check and identify the correctly annotated text.

### **5.**  **Train and evaluate the template dataset on Tensorflow Neural Machine translation with attention** [**model**](https://www.blogger.com/u/1/blog/post/edit/7948183821104122808/789201015065518066#) **.**

As the final step, the NMT model was trained on the correctly annotated training dataset and evaluated on the correctly annotated test dataset. The results were bad since the training dataset is small.

### **Conclusion**

- The used dataset is small and using the entity annotation method we used the dataset became even smaller. Therefore the model was not able to recognize patterns.
- Since the dataset is small, the vocabulary was small and when it comes to translation &#39;Key Errors&#39; were thrown.

### **Future work**

- Try different datasets.
- Try annotating the input language and target language texts separately using DBpedia spotlight.