## Informal Competency Questions (Iteration 11)

## Question 1

### Identifier
CQ_11.1

### Question
Return all multimedia content available in the platform.

### Expected Outcome
A list of all multimedia objects with their types and titles.

### Result
* `multimedia-001` → MediaObject (Introduction to Medieval History: The Carolingian Renaissance)
* `multimedia-002` → MediaObject (Oral History: Resistance Movement in WWII Italy)
* `multimedia-003` → MediaObject (High-Resolution Scan: Botticelli's Birth of Venus)

### Based on
Example 1, Example 2, and Example 3


## Question 2

### Identifier
CQ_11.2

### Question
Return all video content with their duration and encoding format.

### Expected Outcome
A list of video objects with technical metadata.

### Result
* `multimedia-001` → PT1H25M30S, video/mp4

### Based on
Example 1


## Question 3

### Identifier
CQ_11.3

### Question
Return all multimedia content with their file size and access conditions.

### Expected Outcome
A list of multimedia objects with storage and access information.

### Result
* `multimedia-001` → 1.2 GB, Open Access
* `multimedia-002` → 198 MB, Open Access
* `multimedia-003` → 850 MB, Restricted access or use

### Based on
Example 1, Example 2, and Example 3


## Question 4

### Identifier
CQ_11.4

### Question
Return all multimedia content classified under History.

### Expected Outcome
A list of multimedia objects related to medieval studies.

### Result
* `multimedia-001` → Introduction to Medieval History: The Carolingian Renaissance

### Based on
Example 1


## Question 5

### Identifier
CQ_11.5

### Question
Return all audio recordings with their language and temporal coverage.

### Expected Outcome
A list of audio objects with linguistic and chronological metadata.

### Result
* `multimedia-002` → Italian/English, 1943-1945

### Based on
Example 2


## Question 6

### Identifier
CQ_11.6

### Question
Return all multimedia content with their providers.

### Expected Outcome
A list of multimedia objects with distribution information.

### Result
* `multimedia-001` → Provider: Canal-U
* `multimedia-002` → Provider: ISIDORE
* `multimedia-003` → Provider: Europeana

### Based on
Example 1, Example 2, and Example 3


## Question 7

### Identifier
CQ_11.7

### Question
Return all multimedia content with Creative Commons licenses.

### Expected Outcome
A list of multimedia objects with CC licensing information.

### Result
* `multimedia-001` → Creative Commons
* `multimedia-002` → Creative Commons
* `multimedia-003` → Creative Commons

### Based on
Example 1, Example 2, and Example 3


## Question 8

### Identifier
CQ_11.8

### Question
Return all multimedia content with their spatial coverage and subjects.

### Expected Outcome
A list of multimedia objects with geographical and topical information.

### Result
* `multimedia-001` → Europe occidentale, medieval history
* `multimedia-002` → Italy, European history
* `multimedia-003` → Florence Italy, art history

### Based on
Example 1, Example 2, and Example 3


## Question 9

### Identifier
CQ_11.9

### Question
Return all multimedia content that references other documents.

### Expected Outcome
A list of multimedia objects with bibliographic references.

### Result
* `multimedia-001` → Medieval Studies Anthology 2023
* `multimedia-003` → Digital Analysis of Botticelli's Techniques

### Based on
Example 1 and Example 3


## Question 10

### Identifier
CQ_11.10

### Question
Return all multimedia content with their descriptive keywords.

### Expected Outcome
A list of multimedia objects with their associated keyword terms.

### Result
* `multimedia-001` → histoire médiévale, renaissance carolingienne, Charlemagne
* `multimedia-002` → oral history, World War II, Italian Resistance, memory studies
* `multimedia-003` → Renaissance art, Botticelli, digital humanities, cultural heritage

### Based on
Example 1, Example 2, and Example 3


## Question 11

### Identifier
CQ_11.11

### Question
Return all multimedia content that have DOI identifiers by identifier scheme.

### Expected Outcome
A list of multimedia objects with valid DOI identifiers.

### Result
* `multimedia-001` → 10.5281/zenodo.video.medieval.carolingian
* `multimedia-002` → 10.5281/zenodo.audio.resistance.interview
* `multimedia-003` → 10.5281/zenodo.image.birth.venus.hd

### Based on
Example 1, Example 2, and Example 3


## Question 12

### Identifier
CQ_11.12

### Question
Return all multimedia content that have Handle identifiers by identifier scheme.

### Expected Outcome
A list of multimedia objects with valid Handle identifiers.

### Result
* `multimedia-001` → 21.11130/00-VIDEO-MEDIEVAL-CAROLINGIAN
* `multimedia-002` → 21.11130/00-AUDIO-RESISTANCE-INTERVIEW
* `multimedia-003` → 21.11130/00-IMAGE-BIRTH-VENUS-HD

### Based on
Example 1, Example 2, and Example 3


## Question 13

### Identifier
CQ_11.13

### Question
Return all multimedia content with platform identifiers by type.

### Expected Outcome
A list of multimedia objects with their internal platform identifiers categorized by type.

### Result
* `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → `triple:internal_id_schema` → "TRIPLE_MEDIA_VIDEO_001"
* `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → `datacite:ark` → "ark:/12345/media-video-medieval-carolingian"
* `triple:multimedia-001` → "Introduction to Medieval History: The Carolingian Renaissance" → `triple:original_id_schema` → "canal_u_video_12345"
* `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → `triple:internal_id_schema` → "TRIPLE_MEDIA_AUDIO_002"
* `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → `datacite:ark` → "ark:/12345/media-audio-resistance-interview"
* `triple:multimedia-002` → "Oral History: Resistance Movement in WWII Italy" → `triple:original_id_schema` → "memory_inst_audio_789"
* `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → `triple:internal_id_schema` → "TRIPLE_MEDIA_IMAGE_003"
* `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → `datacite:ark` → "ark:/12345/media-image-birth-venus-hd"
* `triple:multimedia-003` → "High-Resolution Scan: Botticelli's Birth of Venus" → `triple:original_id_schema` → "uffizi_digital_venus_hd"

### Based on
Example 1, Example 2, and Example 3
