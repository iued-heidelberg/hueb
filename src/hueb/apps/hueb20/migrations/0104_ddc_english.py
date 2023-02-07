from django.db import migrations


def fill_ddc_english(apps, schema_editor):
    DdcGerman = apps.get_model("hueb20", "DdcGerman")

    ddc_english_list = DDC_ENGLISH.split("\n")
    ddc_english = {
        item.split(" ", 1)[0]: item.split(" ", 1)[1] for item in ddc_english_list
    }

    for ddc in DdcGerman.objects.all():
        try:
            ddc.ddc_name_en = ddc_english[ddc.ddc_number]
        except KeyError:
            ddc.ddc_name_en = "[Unassigned]"
        ddc.save()


def empty_transl_name(apps, schema_editor):
    DdcGerman = apps.get_model("hueb20", "DdcGerman")

    for ddc in DdcGerman.objects.all():
        ddc.ddc_name_en = ddc.ddc_name_temp
        ddc.save()


class Migration(migrations.Migration):
    dependencies = [
        ("hueb20", "0103_fill_translated_languages"),
    ]

    operations = [migrations.RunPython(fill_ddc_english, empty_transl_name)]


DDC_ENGLISH = """000 Computer science, information and general works
001 Knowledge
002 The book (writing, libraries, and book-related topics)
003 Systems
004 Data processing and computer science
005 Computer programming, programs and data
006 Special computer methods (e.g. AI, multimedia, VR)
007 [Unassigned]
008 [Unassigned]
009 [Unassigned]
010 Bibliographies
010 Bibliography
011 Bibliographies
012 Bibliographies of individuals
013 [Unassigned]
014 Bibliographies of anonymous and pseudonymous works
015 Bibliographies of works from specific places
016 Bibliographies of works on specific subjects
017 General subject catalogs
018 Catalogs arranged by author, date, etc.
019 Dictionary catalogs
020 Library and information sciences
020 Library and information sciences
021 Library relationships (with archives, information centers, etc.)
022 Administration of physical plant
023 Personnel management
024 [Unassigned]
025 Library operations
026 Libraries for specific subjects
027 General libraries
028 Reading and use of other information media
029 [Unassigned]
030 Encyclopedias and books of facts
030 General encyclopedic works
031 Encyclopedias in American English
032 Encyclopedias in English
033 Encyclopedias in other Germanic languages
034 Encyclopedias in French, Occitan, and Catalan
035 Encyclopedias in Italian, Romanian, and related languages
036 Encyclopedias in Spanish and Portuguese
037 Encyclopedias in Slavic languages
038 Encyclopedias in Scandinavian languages
039 Encyclopedias in other languages
040 [Unassigned] (formerly Biographies)
050 Magazines, journals and serials
050 General serial publications
051 Serials in American English
052 Serials in English
053 Serials in other Germanic languages
054 Serials in French, Occitan, and Catalan
055 Serials in Italian, Romanian, and related languages
056 Serials in Spanish and Portuguese
057 Serials in Slavic languages
058 Serials in Scandinavian languages
059 Serials in other languages
060 Associations, organizations and museums
060 General organizations and museum science
061 Organizations in North America
062 Organizations in British Isles; in England
063 Organizations in central Europe; in Germany
064 Organizations in France and Monaco
065 Organizations in Italy and adjacent islands
066 Organizations in Iberian peninsula and adjacent islands
067 Organizations in eastern Europe; in Russia
068 Organizations in other geographic areas
069 Museum science
070 News media, journalism and publishing
070 News media, journalism, and publishing
071 Newspapers in North America
072 Newspapers in British Isles; in England
073 Newspapers in central Europe; in Germany
074 Newspapers in France and Monaco
075 Newspapers in Italy and adjacent islands
076 Newspapers in Iberian peninsula and adjacent islands
077 Newspapers in eastern Europe; in Russia
078 Newspapers in Scandinavia
079 Newspapers in other geographic areas
080 Quotations
080 General collections
081 Collections in American English
082 Collections in English
083 Collections in other Germanic languages
084 Collections in French, Occitan, Catalan
085 Collections in Italian, Romanian, and related languages
086 Collections in Spanish and Portuguese
087 Collections in Slavic languages
088 Collections in Scandinavian languages
089 Collections in other languages
090 Manuscripts and rare books
090 Manuscripts and rare books
091 Manuscripts
092 Block books
093 Incunabula
094 Printed books
095 Books notable for bindings
096 Books notable for illustrations
097 Books notable for ownership or origin
098 Prohibited works, forgeries, and hoaxes
099 Books notable for format
100 Philosophy and psychology
101 Theory of philosophy
102 Miscellany
103 Dictionaries and encyclopedias
104 No longer used — formerly "Essays"
105 Serial publications
106 Organizations and management
107 Education, research, related topics of philosophy
108 Groups of people
109 History and collected biography
110 Metaphysics
110 Metaphysics
111 Ontology
112 No longer used — formerly Methodology
113 Cosmology (Philosophy of nature)
114 Space
115 Time
116 Change
117 Structure
118 Force and energy
119 Number and quantity
120 Epistemology
120 Epistemology, causation, and humankind
121 Epistemology (Theory of knowledge)
122 Causation
123 Determinism and indeterminism
124 Teleology
125 No longer used — formerly Infinity
126 The self
127 The unconscious and the subconscious
128 Humankind
129 Origin and destiny of individual souls
130 Parapsychology and occultism
130 Parapsychology and occultism
131 Parapsychological and occult methods for achieving well-being, happiness, success
132 No longer used — formerly "Mental derangements"
133 Specific topics in parapsychology and occultism
134 No longer used — formerly "Mesmerism and Clairvoyance"
135 Dreams and mysteries
136 No longer used — formerly "Mental characteristics"
137 Divinatory graphology
138 Physiognomy
139 Phrenology
140 Philosophical schools of thought
140 Specific philosophical schools and viewpoints
141 Idealism and related systems and doctrines
142 Critical philosophy
143 Bergsonism and intuitionism
144 Humanism and related systems and doctrines
145 Sensationalism
146 Naturalism and related systems and doctrines
147 Pantheism and related systems and doctrines
148 Dogmatism, eclecticism, liberalism, syncretism, and traditionalism
149 Other philosophical systems and doctrines
150 Psychology
150 Psychology
151 No longer used — formerly "Intellect"
152 Sensory perception, movement, emotions, and physiological drives
153 Conscious mental processes and intelligence
154 Subconscious and altered states and processes
155 Differential and developmental psychology
156 Comparative psychology
157 No longer used — formerly "Emotions"
158 Applied psychology
159 No longer used — formerly "Will"
160 Philosophical logic
160 Philosophical logic
161 Induction
162 Deduction
163 [Unassigned]
164 [Unassigned]
165 Fallacies and sources of error
166 Syllogisms
167 Hypotheses
168 Argument and persuasion
169 Analogy
170 Ethics
170 Ethics (Moral philosophy)
171 Ethical systems
172 Political ethics
173 Ethics of family relationships
174 Occupational ethics
175 Ethics of recreation, leisure, public performances, communication
176 Ethics of sex and reproduction
177 Ethics of social relations
178 Ethics of consumption
179 Other ethical norms
180 Ancient, medieval, and Eastern philosophy
180 Ancient, medieval, eastern philosophy
181 Eastern philosophy
182 Pre-Socratic Greek philosophies
183 Sophistic, Socratic, related Greek philosophies
184 Platonic philosophy
185 Aristotelian philosophy
186 Skeptic and Neoplatonic philosophies
187 Epicurean philosophy
188 Stoic philosophy
189 Medieval Western philosophy
190 Modern Western philosophy (19th-century, 20th-century)
190 Modern Western and other noneastern philosophy
191 Philosophy of the United States and Canada
192 Philosophy of the British Isles
193 Philosophy of Germany and Austria
194 Philosophy of France
195 Philosophy of Italy
196 Philosophy of Spain and Portugal
197 Philosophy of Russia
198 Philosophy of Scandinavia and Finland
199 Philosophy in other geographic areas
200 Religion
201 Religious mythology, general classes of religion, interreligious relations and attitudes, social theology
202 Doctrines
203 Public worship and other practices
204 Religious experience, life, practice
205 Religious ethics
206 Leaders and organization
207 Missions and religious education
208 Sources
209 Sects and reform movements
210 Philosophy and theory of religion
210 Philosophy and theory of religion
211 Concepts of God
212 Existence, ways of knowing God, attributes of God
213 Creation
214 Theodicy
215 Science and religion
216 No longer used—formerly Evil
217 No longer used—formerly Prayer
218 Humankind
219 No longer used—formerly Analogies
220 The Bible
220 Bible
221 Old Testament (Tanakh)
222 Historical books of Old Testament
223 Poetic books of Old Testament
224 Prophetic books of Old Testament
225 New Testament
226 Gospels and Acts
227 Epistles
228 Revelation (Apocalypse)
229 Apocrypha, pseudepigrapha, and inter-testamental works
230 Christianity
230 Christianity
231 God
232 Jesus Christ and his family
233 Humankind
234 Salvation and grace
235 Spiritual beings
236 Eschatology
237 No longer used—formerly Future state
238 Creeds, confessions of faith, covenants, and catechisms
239 Apologetics and polemics
240 Christian practice and observance
240 Christian moral and devotional theology
241 Christian ethics
242 Devotional literature
243 Evangelistic writings for individuals and families
244 No longer used—formerly Religious fiction
245 No longer used—formerly Hymnology
246 Use of art in Christianity
247 Church furnishings and related articles
248 Christian experience, practice, life
249 Christian observances in family life
250 Christian orders and local church
250 Local Christian church and Christian religious orders
251 Preaching (Homiletics)
252 Texts of sermons
253 Pastoral office and work (Pastoral theology)
254 Parish administration
255 Religious congregations and orders
256 No longer used — formerly "Religious societies"
257 No longer used — formerly "Parochial schools, libraries", etc.
258 No longer used — formerly "Parochial medicine"
259 Pastoral care of families, of specific groups of people
260 Social and ecclesiastical theology
260 Christian social and ecclesiastical theology
261 Social theology and interreligious relations and attitudes
262 Ecclesiology
263 Days, times, places of religious observance
264 Public worship
265 Sacraments, other rites and acts
266 Missions
267 Associations for religious work
268 Religious education
269 Spiritual renewal
270 History of Christianity
270 History, geographic treatment, biography of Christianity
271 Religious congregations and orders in church history
272 Persecutions in church history
273 Doctrinal controversies and heresies in general church history
274 Christianity in Europe
275 Christianity in Asia
276 Christianity in Africa
277 Christianity in North America
278 Christianity in South America
279 History of Christianity in other areas
280 Christian denominations
280 Denominations and sects of Christian church
281 Early church and Eastern churches
282 Roman Catholic Church
283 Anglican churches
284 Protestant denominations of Continental origin and related body
285 Presbyterian churches, Reformed churches centered in America, Congregational churches
286 Baptist, Restoration Movement, Adventist churches
287 Methodist churches; churches related to Methodism
288 No longer used — formerly "Unitarian"
289 Other denominations and sects
290 Other religions
290 Other religions
291 No longer used — formerly "Comparative religion"
292 Classical religion (Greek and Roman religion)
293 Germanic religion
294 Religions of Indic origin
295 Zoroastrianism (Mazdaism, Parseeism)
296 Judaism
297 Islam, Bábism and Baháʼí Faith
298 No longer used — formerly "Mormonism"
299 Religions not provided for elsewhere
300 Social sciences
301 Sociology and anthropology
302 Social interaction
303 Social processes
304 Factors affecting social behavior
305 Groups of people
306 Culture and institutions
307 Communities
308 No longer used — formerly "Polygraphy"
309 No longer used — formerly "History of sociology"
310 Statistics
310 Collections of general statistics
311 No longer used — formerly "Theory and methods"
312 No longer used — formerly "Population"
313 No longer used — formerly "Special topics"
314 General statistics of Europe
315 General statistics of Asia
316 General statistics of Africa
317 General statistics of North America
318 General statistics of South America
319 General statistics of Australasia, Pacific Ocean islands, Atlantic Ocean islands, Arctic islands, Antarctica
320 Political science
320 Political science (Politics and government)
321 Systems of governments and states
322 Relation of state to organized groups and their members
323 Civil and political rights
324 The political process
325 International migration and colonization
326 Slavery and emancipation
327 International relations
328 The legislative process
329 [Unassigned]
330 Economics
330 Economics
331 Labor economics
332 Financial economics
333 Economics of land and energy
334 Cooperatives
335 Socialism and related systems
336 Public finance
337 International economics
338 Production
339 Macroeconomics and related topics
340 Law
340 Law
341 Law of nations
342 Constitutional and administrative law
343 Military, defense, public property, public finance, tax, commerce (trade), industrial law
344 Labor, social service, education, cultural law
345 Criminal law
346 Private law
347 Procedure and courts
348 Laws, regulations, cases
349 Law of specific jurisdictions, areas, socioeconomic regions, regional intergovernmental organizations
350 Public administration and military science
350 Public administration and military science
351 Public administration
352 General considerations of public administration
353 Specific fields of public administration
354 Public administration of economy and environment
355 Military science
356 Foot forces and warfare
357 Mounted forces and warfare
358 Air and other specialized forces and warfare; engineering and related services
359 Sea forces and warfare
360 Social problems and social services
360 Social problems and services; associations
361 Social problems and services
362 Social problems of and services to groups of people
363 Other social problems and services
364 Criminology
365 Penal and related institutions
366 Secret associations and societies
367 General clubs
368 Insurance
369 Associations
370 Education
370 Education
371 Schools and their activities, special education
372 Primary education (elementary education)
373 Secondary education
374 Adult education
375 Curricula
376 No longer used — formerly "Education of women"
377 No longer used — formerly "Ethical education"
378 Higher education (Tertiary education)
379 Public policy issues in education
380 Commerce, communications and transportation
380 Commerce, communications transportation
381 Commerce (Trade)
382 International commerce (Foreign trade)
383 Postal communication
384 Communications
385 Railroad transportation
386 Inland waterway and ferry transportation
387 Water, air, space transportation
388 Transportation
389 Metrology and standardization
390 Customs, etiquette and folklore
390 Customs, etiquette, folklore
391 Costume and personal appearance
392 Customs of life cycle and domestic life
393 Death customs
394 General customs
395 Etiquette (Manners)
396 No longer used — formerly "Women's position and treatment"
397 No longer used — formerly "outcast studies"
398 Folklore
399 Customs of war and diplomacy
400 Language
401 Philosophy and theory, international languages
402 Miscellany
403 Dictionaries, encyclopedias, concordances
404 Special topics of language
405 Serial publications
406 Organizations and management
407 Education, research, related topics
408 Groups of people
409 Geographic treatment and biography
410 Linguistics
410 Linguistics
411 Writing systems of standard forms of languages
412 Etymology of standard forms of languages
413 Dictionaries of standard forms of languages
414 Phonology and phonetics of standard forms of languages
415 Grammar of standard forms of languages
416 No longer used — formerly "Prosody"
417 Dialectology and historical linguistics
418 Standard usage (Prescriptive linguistics)
419 Sign languages
420 English and Old English languages
420 English and Old English (Anglo-Saxon)
421 Writing system, phonology, phonetics of standard English
422 Etymology of standard English
423 Dictionaries of standard English
424 No longer used — formerly "English thesauruses"
425 Grammar of standard English
426 No longer used — formerly "English prosodies"
427 Historical and geographical variations, modern nongeographic variations of English
428 Standard English usage (Prescriptive linguistics)
429 Old English (Anglo-Saxon)
430 German and related languages
430 German and related languages
431 Writing systems, phonology, phonetics of standard German
432 Etymology of standard German
433 Dictionaries of standard German
434 [Unassigned]
435 Grammar of standard German
436 [Unassigned]
437 Historical and geographic variations, modern nongeographic variations of German
438 Standard German usage (Prescriptive linguistics)
439 Other Germanic languages
440 French and related languages
440 French and related Romance languages
441 Writing systems, phonology, phonetics of standard French
442 Etymology of standard French
443 Dictionaries of standard French
444 [Unassigned]
445 Grammar of standard French
446 [Unassigned]
447 Historical and geographic variations, modern nongeographic variations of French
448 Standard French usage (Prescriptive linguistics)
449 Occitan Catalan, Franco-Provençal
450 Italian, Romanian and related languages
450 Italian, Dalmatian, Romanian, Rhaetian, Sardinian, Corsican
451 Writing systems, phonology, phonetics of standard Italian
452 Etymology of standard Italian
453 Dictionaries of standard Italian
454 [Unassigned]
455 Grammar of standard Italian
456 [Unassigned]
457 Historical and geographic variations, modern nongeographic variations of Italian
458 Standard Italian usage (Prescriptive linguistics)
459 Romanian, Rhaetian, Sardinian, Corsican
460 Spanish, Portuguese, Galician
460 Spanish, Portuguese, Galician
461 Writing systems, phonology, phonetics of standard Spanish
462 Etymology of standard Spanish
463 Dictionaries of standard Spanish
464 [Unassigned]
465 Grammar of standard Spanish
466 [Unassigned]
467 Historical and geographic variations, modern nongeographic variations of Spanish
468 Standard Spanish usage (Prescriptive linguistics)
469 Portuguese
470 Latin and Italic languages
470 Latin and related Italic languages
471 Writing systems, phonology, phonetics of classical Latin
472 Etymology of classical Latin
473 Dictionaries of classical Latin
474 [Unassigned]
475 Grammar of classical Latin
476 [Unassigned]
477 Old, postclassical, Vulgar Latin
478 Classical Latin usage (Prescriptive linguistics)
479 Other Italic languages
480 Classical and modern Greek languages
480 Classical Greek and related Hellenic languages
481 Writing systems, phonology, phonetics of classical Greek
482 Etymology of classical Greek
483 Dictionaries of classical Greek
484 [Unassigned]
485 Grammar of classical Greek
486 [Unassigned]
487 Preclassical and postclassical Greek
488 Classical Greek usage (Prescriptive linguistics)
489 Other Hellenic languages
490 Other languages
490 Other languages
491 East Indo-European and Celtic languages
492 Afro-Asiatic languages
493 Non-Semitic Afro-Asiatic languages
494 Altic, Uralic, Hyperborean, Dravidian languages, miscellaneous languages of south Asia
495 Languages of East and Southeast Asia
496 African languages
497 North American native languages
498 South American native languages
499 Non-Austronesian languages of Oceania, Austronesian languages, miscellaneous languages
500 Science
500 Natural sciences and mathematics
501 Philosophy and theory
502 Miscellany
503 Dictionaries, encyclopedias, concordances
504 [Unassigned]
505 Serial publications
506 Organizations and management
507 Education, research, related topics
508 Natural history
509 History, geographic treatment, biography
510 Mathematics
510 Mathematics
511 General principles of mathematics
512 Algebra
513 Arithmetic
514 Topology
515 Analysis
516 Geometry
517 [Unassigned]
518 Numerical analysis
519 Probabilities and applied mathematics
520 Astronomy
520 Astronomy and allied sciences
521 Celestial mechanics
522 Techniques, procedures, apparatus, equipment, materials
523 Specific celestial bodies and phenomena
524 [Unassigned]
525 Earth (Astronomical geography)
526 Mathematical geography
527 Celestial navigation
528 Ephemerides
529 Chronology
530 Physics
530 Physics
531 Classical mechanics
532 Fluid mechanics
533 Pneumatics (Gas mechanics)
534 Sound and related vibrations
535 Light and related radiation
536 Heat
537 Electricity and electronics
538 Magnetism
539 Modern physics
540 Chemistry
540 Chemistry and allied sciences
541 Physical chemistry
542 Techniques, procedures, apparatus, equipment, materials
543 Analytical chemistry
544 No longer used — formerly "Qualitative analysis"
545 No longer used — formerly "Quantitative analysis"
546 Inorganic chemistry
547 Organic chemistry
548 Crystallography
549 Mineralogy
550 Earth sciences and geology
550 Earth sciences
551 Geology, hydrology, meteorology
552 Petrology
553 Economic geology
554 Earth sciences of Europe
555 Earth sciences of Asia
556 Earth sciences of Africa
557 Earth sciences of North America
558 Earth sciences of South America
559 Earth sciences of Australasia, Pacific Ocean islands, Atlantic Ocean islands, Arctic islands, Antarctica, extraterrestrial worlds
560 Fossils and prehistoric life
560 Paleontology
561 Paleobotany, fossil microorganisms
562 Fossil invertebrates
563 Miscellaneous fossil marine and seashore invertebrates
564 Fossil Mollusca and Molluscoidea
565 Fossil Arthropoda
566 Fossil Chordata
567 Fossil cold-blooded vertebrates
568 Fossil Aves (birds)
569 Fossil Mammalia
570 Biology
570 Biology
571 Physiology and related subjects
572 Biochemistry
573 Specific physiological systems in animals, regional histology and physiology in animals
574 [Unassigned]
575 Specific parts of and physiological systems in plants
576 Genetics and evolution
577 Ecology
578 Natural history of organisms and related subjects
579 Natural history of microorganisms, fungi, algae
580 Plants
580 Plants
581 Specific topics in natural history of plants
582 Plants noted for specific vegetative characteristics and flowers
583 Magnoliopsida (Dicotyledones)
584 Liliopsida (Monocotyledones)
585 Pinophyta (Gymnosperms)
586 Cryptogamia (Seedless plants)
587 Pteridophyta
588 Bryophyta
589 No longer used—formerly Forestry
590 Animals (Zoology)
590 Animals
591 Specific topics in natural history of animals
592 Invertebrates
593 Miscellaneous marine and seashore invertebrates
594 Mollusca and Molluscoidea
595 Arthropoda
596 Chordata
597 Cold-blooded vertebrates
598 Aves (Birds)
599 Mammalia (Mammals)
600 Technology
600 Technology (Applied sciences)
601 Philosophy and theory
602 Miscellany
603 Dictionaries, encyclopedias, concordances
604 Technical drawing, hazardous materials technology; groups of people
605 Serial publications
606 Organizations
607 Education, research, related topics
608 Patents
609 History, geographic treatment, biography
610 Medicine and health
610 Medicine and health
611 Human anatomy, cytology, histology
612 Human physiology
613 Personal health and safety
614 Forensic medicine; incidence of injuries, wounds, disease; public preventive medicine
615 Pharmacology and therapeutics
616 Diseases
617 Surgery, regional medicine, dentistry, ophthalmology, otology, audiology
618 Gynecology, obstetrics, pediatrics, geriatrics
619 No longer used—formerly Experimental medicine
620 Engineering
620 Engineering and applied operations
621 Applied physics
622 Mining and related operations
623 Military and nautical engineering
624 Civil engineering
625 Engineering of railroads, roads
626 [Unassigned]
627 Hydraulic engineering
628 Sanitary engineering
629 Other branches of engineering
630 Agriculture
630 Agriculture and related technologies
631 Specific techniques; apparatus, equipment, materials
632 Plant injuries, diseases, pests
633 Field and plantation crops
634 Orchards, fruits, forestry
635 Garden crops (Horticulture)
636 Animal husbandry
637 Processing dairy and related products
638 Insect culture
639 Hunting, fishing, conservation, related technologies
640 Home and family management
640 Home and family management
641 Food and drink
642 Meals and table service
643 Housing and household equipment
644 Household utilities
645 Household furnishings
646 Sewing, clothing, management of personal and family life
647 Management of public households (Institutional housekeeping)
648 Housekeeping
649 Child rearing; home care of people with disabilities and illnesses
650 Management and public relations
650 Management and auxiliary services
651 Office services
652 Processes of written communication
653 Shorthand
654 [Unassigned]
655 [Unassigned]
656 [Unassigned]
657 Accounting
658 General management
659 Advertising and public relations
660 Chemical engineering
660 Chemical engineering and related technologies
661 Technology of industrial chemicals
662 Technology of explosives, fuels, related products
663 Beverage technology
664 Food technology
665 Technology of industrial oils, fats, waxes, gases
666 Ceramic and allied technologies
667 Cleaning, color, coating, related technologies
668 Technology of other organic products
669 Metallurgy
670 Manufacturing
670 Manufacturing
671 Metalworking processes and primary metal products
672 Iron, steel, other iron alloys
673 Nonferrous metals
674 Lumber processing, wood products, cork
675 Leather and fur processing
676 Pulp and paper technology
677 Textiles
678 Elastomers and elastomer products
679 Other products of specific kinds of materials
680 Manufacture for specific uses
680 Manufacture of products for specific uses
681 Precision instruments and other devices
682 Small forge work (Blacksmithing)
683 Hardware and household appliances
684 Furnishings and home workshops
685 Leather and fur goods, and related products
686 Printing and related activities
687 Clothing and accessories
688 Other final products, and packaging technology
689 [Unassigned]
690 Construction of buildings
690 Construction of buildings
691 Building materials
692 Auxiliary construction practices
693 Construction in specific types of materials and for specific purposes
694 Wood construction
695 Roof covering
696 Utilities
697 Heating, ventilating, air-conditioning engineering
698 Detail finishing
699 [Unassigned]
700 The Arts
701 Philosophy and theory of fine and decorative arts
702 Miscellany of fine and decorative arts
703 Dictionaries, encyclopedias, concordances of fine and decorative arts
704 Special topics in fine and decorative arts
705 Serial publications of fine and decorative arts
706 Organizations and management of fine and decorative arts
707 Education, research, related topics of fine and decorative arts
708 Galleries, museums, private collections of fine and decorative arts
709 History, geographic treatment, biography
710 Area planning and landscape architecture
710 Area planning and landscape architecture
711 Area planning (Civic art)
712 Landscape architecture (Landscape design)
713 Landscape architecture of trafficways
714 Water features in landscape architecture
715 Woody plants in landscape architecture
716 Herbaceous plants in landscape architecture
717 Structures in landscape architecture
718 Landscape design of cemeteries
719 Natural landscapes
720 Architecture
720 Architecture
721 Architectural materials and structural elements
722 Architecture from earliest times to c. 300
723 Architecture from c. 300 to 1399
724 Architecture from 1400
725 Public structures
726 Buildings for religious and related purposes
727 Buildings for educational and research purposes
728 Residential and related buildings
729 Design and decoration of structures and accessories
730 Sculpture, ceramics and metalwork
730 Sculpture and related arts
731 Processes, forms, subjects of sculpture
732 Sculpture from earliest times to c. 500, sculpture of non-literate peoples
733 Greek, Etruscan, Roman sculpture
734 Sculpture from ca 500 to 1399
735 Sculpture from 1400
736 Carving and carvings
737 Numismatics and sigillography
738 Ceramic arts
739 Art metalwork
740 Graphic arts and decorative arts
740 Graphic arts
741 Drawing and drawings
742 Perspective in drawing
743 Drawing and drawings by subject
744 [Unassigned]
745 Decorative arts
746 Textile arts
747 Interior decoration
748 Glass
749 Furniture and accessories
750 Painting
750 Painting and paintings
751 Techniques, procedures, apparatus, equipment, materials, forms
752 Color
753 Symbolism, allegory, mythology, legend
754 Genre paintings
755 Religion
756 [Unassigned]
757 Human figures
758 Nature, architectural subjects and cityscapes, other specific subjects
759 History, geographic treatment, biography
760 Printmaking and prints
760 Printmaking and prints
761 Relief processes (Block printing)
762 [Unassigned]
763 Lithographic processes (Planographic processes)
764 Chromolithography and serigraphy
765 Metal engraving
766 Mezzotinting, aquatinting, and related processes
767 Etching and drypoint
768 [Unassigned]
769 Prints
770 Photography, computer art, film, video
770 Photography, computer art, cinematography, videography
771 Techniques, procedures, apparatus, equipment, materials
772 Metallic salt processes
773 Pigment processes of printing
774 No longer used—formerly Holography
775 No longer used—formerly Digital photography
776 Computer art (Digital art)
777 Cinematography and Videography
778 Specific fields and special kinds of photography
779 Photographic images
780 Music
780 Music
781 General principles and musical forms
782 Vocal music
783 Music for single voices
784 Instruments and Instrumental ensembles and their music
785 Ensembles with only one instrument per part
786 Keyboard, mechanical, electrophonic, percussion instruments
787 Stringed instruments (Chordophones)
788 Wind instruments (Aerophones)
789 [Unassigned]
790 Outline of sports, games and entertainment
790 Recreational and performing arts
791 Public performances
792 Stage presentations
793 Indoor games and amusements
794 Indoor games of skill
795 Games of chance
796 Athletic and outdoor sports and games
797 Aquatic and air sports
798 Equestrian sports and animal racing
799 Fishing, hunting, shooting
800 Literature (Belles-lettres) and rhetoric
801 Philosophy and theory
802 Miscellany
803 Dictionaries, encyclopedias, concordances
804 [Unassigned]
805 Serial publications
806 Organizations and management
807 Education, research, related topics
808 Rhetoric and collections of literary texts from more than two literatures
809 History, description, critical appraisal of more than two literatures
810 American literature in English
810 American literature in English
811 American poetry in English
812 American drama in English
813 American fiction in English
814 American essays in English
815 American speeches in English
816 American letters in English
817 American humor and satire in English
818 American miscellaneous writings in English
819 [Unassigned]
820 English and Old English literatures
820 English and Old English (Anglo-Saxon) literatures
821 English Poetry
822 English drama
823 English fiction
824 English essays
825 English speeches
826 English letters
827 English humor and satire
828 English miscellaneous writings
829 Old English (Anglo-Saxon) literature
830 German and related literatures
830 German literature and literatures of related languages
831 German poetry
832 German drama
833 German fiction
834 German essays
835 German speeches
836 German letters
837 German humor and satire
838 German miscellaneous writings
839 Other Germanic literatures
840 French and related literatures
840 French literature and literatures of related Romance languages
841 French poetry
842 French drama
843 French fiction
844 French essays
845 French speeches
846 French letters
847 French humor and satire
848 French miscellaneous writings
849 Occitan, Catalan, Franco-Provençal literatures
850 Italian, Romanian and related literatures
850 Literatures of Italian, Dalmatian, Romanian, Rhaetian, Sardinian, Corsican languages
851 Italian poetry
852 Italian drama
853 Italian fiction
854 Italian essays
855 Italian speeches
856 Italian letters
857 Italian humor and satire
858 Italian miscellaneous writings
859 Literatures of Romanian, Rhaetian, Sardinian, Corsican languages
860 Spanish, Portuguese, Galician literatures
860 Literatures of Spanish, Portuguese, Galician languages
861 Spanish poetry
862 Spanish drama
863 Spanish fiction
864 Spanish essays
865 Spanish speeches
866 Spanish letters
867 Spanish humor and satire
868 Spanish miscellaneous writings
869 Literatures of Portuguese and Galician languages
870 Latin and Italic literatures
870 Latin literature and literatures of related Italic languages
871 Latin poetry
872 Latin dramatic poetry and drama
873 Latin epic poetry and fiction
874 Latin lyric poetry
875 Latin speeches
876 Latin letters
877 Latin humor and satire
878 Latin miscellaneous writings
879 Literatures of other Italic languages
880 Classical and modern Greek literatures
880 Classical Greek literature and literatures of related Hellenic languages
881 Classical Greek poetry
882 Classical Greek drama
883 Classical Greek epic poetry and fiction
884 Classical Greek lyric poetry
885 Classical Greek speeches
886 Classical Greek letters
887 Classical Greek humor and satire
888 Classical Greek miscellaneous writings
889 Modern Greek literature
890 Other literatures
890 Literatures of other specific languages and language families
891 East Indo-European and Celtic literatures
892 Afro-Asiatic literatures
893 Non-Semitic Afro-Asiatic literatures
894 Literatures of Altaic, Uralic, Hyperborean, Dravidian languages; literatures of miscellaneous languages of South Asia
895 Literatures of East and Southeast Asia
896 African literatures
897 Literatures of North American native languages
898 Literatures of South American native languages
899 Literatures of non-Austronesian languages of Oceania, of Austronesian languages, of miscellaneous languages
900 History, geography, and auxiliary disciplines
901 Philosophy and theory of history
902 Miscellany of history
903 Dictionaries, encyclopedias, concordances of history
904 Collected accounts of events
905 Serial publications of history
906 Organizations and management of history
907 Education, research, related topics of history
908 History with respect to groups of people
909 World history
910 Geography and travel
910 Geography and travel
911 Historical geography
912 Graphic representations of surface of earth and of extraterrestrial worlds
913 Geography of and travel in the ancient world
914 Geography of and travel in Europe
915 Geography of and travel in Asia
916 Geography of and travel in Africa
917 Geography of and travel in North America
918 Geography of and travel in South America
919 Geography of and travel in Australasia, Pacific Ocean islands, Atlantic Ocean islands, Arctic islands, Antarctica, and on extraterrestrial worlds
920 Biography and genealogy
920 Biography, genealogy, insignia
921–928 This range is reserved as an optional location for biographies, which are shelved alphabetically by subject's last name.
929 Genealogy, names, insignia
930 History of ancient world (to c. 499)
930 History of ancient world to c. 499
931 China to 420
932 Egypt to 640
933 Palestine to 70
934 South Asia to 647
935 Mesopotamia to 637 and Iranian Plateau to 637
936 Europe north and west of Italian Peninsula to c. 499
937 Italian Peninsula to 476 and adjacent territories to 476
938 Greece to 323
939 Other parts of ancient world
940 History of Europe
940 History of Europe
941 British Isles
942 England and Wales
943 Germany and neighboring central European countries
944 France and Monaco
945 Italy, San Marino, Vatican City, Malta
946 Spain, Andorra, Gibraltar, Portugal
947 Russia and neighboring east European countries
948 Scandinavia
949 Other parts of Europe
950 History of Asia
950 History of Asia
951 China and adjacent areas
952 Japan
953 Arabian Peninsula and adjacent areas
954 India and neighboring south Asian countries;
955 Iran
956 Middle East (Near East)
957 Siberia (Asiatic Russia)
958 Central Asia
959 Southeast Asia
960 History of Africa
960 History of Africa
961 Tunisia and Libya
962 Egypt, Sudan, South Sudan
963 Ethiopia and Eritrea
964 Morocco, Ceuta, Melilla Western Sahara, Canary Islands
965 Algeria
966 West Africa and offshore islands
967 Central Africa and offshore islands
968 Republic of South Africa and neighboring southern African countries
969 South Indian Ocean islands
970 History of North America
970 History of North America
971 Canada
972 Mexico, Central America, West Indies, Bermuda
973 United States
974 Northeastern United States (New England and Middle Atlantic states)
975 Southeastern United States (South Atlantic states)
976 South central United States
977 North central United States
978 Western United States
979 Great Basin and Pacific Slope region of United States
980 History of South America
980 History of South America
981 Brazil
982 Argentina
983 Chile
984 Bolivia
985 Peru
986 Colombia and Ecuador
987 Venezuela
988 Guiana
989 Paraguay and Uruguay
990 History of other areas
990 History of Australasia, Pacific Ocean islands, Atlantic Ocean islands, Arctic islands, Antarctica, extraterrestrial worlds
991 [Unassigned]
992 [Unassigned]
993 New Zealand
994 Australia
995 New Guinea and neighboring countries of Melanesia
996 Polynesia and other Pacific Ocean islands
997 Atlantic Ocean islands
998 Arctic islands and Antarctica
999 Extraterrestrial worlds"""
