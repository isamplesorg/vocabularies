---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
title: "Sampled Feature Type vocabulary"
date: "2023-04-07T07:26:34.437760+00:00"
subtitle: |
  Categories to specify the broad context that a sample is intended to represent.
execute:
  echo: false
---

Namespace: 
[`https://w3id.org/isample/vocabulary/sampledfeature/0.9/sampledfeaturevocabulary`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/sampledfeaturevocabulary)

**History**

* 2021-12-10 SMR add missing skos:inScheme statements
* 2022-01-07 SMR change to https://w3id.org/isample/ uri base, make the ConceptScheme an ontology as well. For uploading to ESIP COR and w3id resolution redirect set up. Add some mappings to other ontologies using seeAlso, closeMatch, narrowMatch.
* 2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes in definitions. Add skos matches to URIs from other vocabularies. Fix typo in glacierenvrionment URI (changed the URI to glacierenvironment)
* Remove Marine biome, Subaerial terrestrial environment, Subaqueous terrestrial environment per github issue https://github.com/isamplesorg/metadata/issues/41. Make Experiment setting and Laboratory or curatorial environemtn  subclasses of Active human occupation site.
* 2022-09-07 SMR update some of the skos mappings to other vocabularies; remove references to other vocabularies as NamedIndividual. Remove rocksample class, it was not linked in hierarchy and inconsistent with design.
* 2022-09-30 add biological entity as sampled feature, per issue https://github.com/isamplesorg/metadata/issues/107. This update was lost at some point and added back in 2022-12-09.

**Concepts**

- [Any sampled feature](#anysampledfeature)
    - [Anthropogenic environment](#anthropogenicenvironment)
        - [Active human occupation site](#activehumanoccupationsite)
            - [Experiment setting](#experimentsetting)
            - [Laboratory or curatorial environment](#laboratorycuratorialenvironment)
        - [Site of past human activities](#pasthumanoccupationsite)
    - [Biological entity](#biologicalentity)
        - [Eukaryote](#eukaryote)
            - [Animalia](#animalia)
                - [Vertebrate ](#vertebrate)
                    - [Amphibian](#amphibian)
                    - [Bird](#bird)
                    - [Fish](#fish)
                    - [Mammal](#mammal)
                    - [Reptile](#reptile)
                - [Arthropod ](#arthropod)
                    - [Arachnid](#arachnid)
                    - [Crustaceans](#crustacea)
                    - [Insect](#hexapoda)
                    - [Myriapod](#myriapod)
                    - [Other arthropod ](#otherarthropod)
                - [Mollusca](#mollusca)
                - [Other invertebrate ](#otherinvertebrate)
                - [Porifera](#porifera)
            - [Fungi](#fungi)
                - [Macrofungi](#macrofungi)
                - [Microfungi](#microfungi)
            - [Plantae](#plantae)
                - [Bryophyte](#bryophyte)
                - [Other plant](#otherplant)
                - [Pteridophyte](#pteridophyte)
                - [Seed plant](#spermatophyte)
            - [Protista](#protista)
                - [Amoebozoa  ](#amoebozoa)
                    - [Myxomycetes](#myxomycete)
                - [Protozoa](#protozoa)
            - [Algae](#algae)
            - [Eukaryotic microorganisms](#eukaryoticmicroorganisms)
        - [Lichen](#lichen)
        - [Plasmid](#plasmid)
        - [Prokaryote](#prokaryote)
            - [Archaea](#archaea)
            - [Bacteria](#bacteria)
        - [Virus](#virus)
            - [Other Virus  ](#othervirus)
            - [Phage](#phage)
    - [Earth environment](#earthenvironment)
        - [Atmosphere](#atmosphere)
        - [Earth interior](#earthinterior)
        - [Earth surface](#earthsurface)
            - [Lake river or stream bottom](#lakeriverstreambottom)
            - [Marine water body bottom](#marinewaterbodybottom)
            - [Subaerial surface environment](#subaerialsurfaceenvironment)
        - [Glacier environment](#glacierenvironment)
        - [Subsurface fluid reservoir](#subsurfacefluidreservoir)
        - [Water body](#waterbody)
            - [Marine environment](#marinewaterbody)
            - [Terrestrial water body](#terrestrialwaterbody)
    - [Extraterrestrial environment](#extraterrestrialenvironment)

##  Any sampled feature

[]{#anysampledfeature}

Concept: [`anysampledfeature`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/anysampledfeature)

Top concept in sampled feature type vocabulary.

###  Anthropogenic environment

[]{#anthropogenicenvironment}

Concept: [`anthropogenicenvironment`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/anthropogenicenvironment)

Child of:
 [`anysampledfeature`](#anysampledfeature)

Sampled feature is produced by or related to human activity past or
present.

####  Active human occupation site

[]{#activehumanoccupationsite}

Concept: [`activehumanoccupationsite`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/activehumanoccupationsite)

Child of:
 [`anthropogenicenvironment`](#anthropogenicenvironment)

Specimen samples materials or objects produced by current or ongoing
human activity

#####  Experiment setting

[]{#experimentsetting}

Concept: [`experimentsetting`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/experimentsetting)

Child of:
 [`activehumanoccupationsite`](#activehumanoccupationsite)

Sampled feature is the expermental set up that produced the sample.

#####  Laboratory or curatorial environment

[]{#laboratorycuratorialenvironment}

Concept: [`laboratorycuratorialenvironment`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/laboratorycuratorialenvironment)

Child of:
 [`activehumanoccupationsite`](#activehumanoccupationsite)

specimen samples environment in a laboratory; e.g. lab blank
measurements.

####  Site of past human activities

[]{#pasthumanoccupationsite}

Concept: [`pasthumanoccupationsite`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/pasthumanoccupationsite)

Child of:
 [`anthropogenicenvironment`](#anthropogenicenvironment)

specimen samples a place where humans have been and left evidence of
their activity. Includes prehistoric and paleo hominid sites

###  Biological entity

[]{#biologicalentity}

Concept: [`biologicalentity`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/biologicalentity)

Child of:
 [`anysampledfeature`](#anysampledfeature)

Sampled feature is an organism. Use for samples that represent some
species of organism as the proximate sampled feature for which the
focus is not the environment that the organism inhabits.

####  Eukaryote

[]{#eukaryote}

Concept: [`eukaryote`](https://w3id.org/isample/vocabulary/biologicentity/0.9/eukaryote)

Child of:
 [`biologicalentity`](#biologicalentity)

organism whose cells have a nucleus. Includes all animals, plants,
fungi, and many unicellular organisms
(https://en.wikipedia.org/wiki/Eukaryote)

#####  Animalia

[]{#animalia}

Concept: [`Animalia`](https://w3id.org/isample/vocabulary/biologicentity/0.9/Animalia)

Child of:
 [`eukaryote`](#eukaryote)

Animals are distinguished from other eukaryotes based on several key
characteristics, including: 1)  animals are multicellular organisms 2)
Animals are heterotrophic, they obtain their food by consuming other
organisms or organic matter; 3) Animals lack cell walls; 4) Many
animals have a nervous system; 5\) Most animals reproduce sexually
(Chat GPT)

######  Vertebrate

[]{#vertebrate}

Concept: [`Vertebrate`](https://w3id.org/isample/vocabulary/biologicentity/0.9/Vertebrate)

Child of:
 [`Animalia`](#Animalia)

Animals that have a vertebral column, a cranium, an endoskeleton, a
well-developed muscular system, and an advanced nervous system
(ChatGPT);

#######  Amphibian

[]{#amphibian}

Concept: [`amphibian`](https://w3id.org/isample/vocabulary/biologicentity/0.9/amphibian)

Child of:
 [`Vertebrate`](#Vertebrate)

Vertebrates that have a dual life cycle, semi-permeable skin, absence
of scales and claws, a three-chambered heart, and dependence on water
for reproduction and survival (ChatGPT)

#######  Bird

[]{#bird}

Concept: [`bird`](https://w3id.org/isample/vocabulary/biologicentity/0.9/bird)

Child of:
 [`Vertebrate`](#Vertebrate)

Vertebrates that have feathers, lightweight, hollow bones, a beak, an
efficient respiratory system, and are warm-blooded. (ChatGPT) {@en}

#######  Fish

[]{#fish}

Concept: [`fish`](https://w3id.org/isample/vocabulary/biologicentity/0.9/fish)

Child of:
 [`Vertebrate`](#Vertebrate)

Vertebrates that have gills, scales, fins, are cold-blooded, and
commonly have a swim bladder; includes jawless fish, cartilaginous
fish and bony fish. (ChatGPT)

#######  Mammal

[]{#mammal}

Concept: [`mammal`](https://w3id.org/isample/vocabulary/biologicentity/0.9/mammal)

Child of:
 [`Vertebrate`](#Vertebrate)

vertebrates that have mammary glands, hair or fur, three middle ear
bones, specialized teeth, and are warm-blooded. (ChatGPT)

#######  Reptile

[]{#reptile}

Concept: [`reptile`](https://w3id.org/isample/vocabulary/biologicentity/0.9/reptile)

Child of:
 [`Vertebrate`](#Vertebrate)

Vertebrates that have scaly skin and claws, amniotic eggs, are cold-
blooded, and are ectothermic (ChatGPT)

######  Arthropod

[]{#arthropod}

Concept: [`arthropod`](https://w3id.org/isample/vocabulary/biologicentity/0.9/arthropod)

Child of:
 [`Animalia`](#Animalia)

invertebrate animals with an exoskeleton, a segmented body, and paired
jointed appendages. Arthropods form the phylum Arthropoda. They are
distinguished by their jointed limbs and cuticle made of chitin, often
mineralised with calcium carbonate. The arthropod body plan consists
of segments, each with a pair of appendages. Arthropods are
bilaterally symmetrical and their body possesses an external skeleton.
(https://en.wikipedia.org/wiki/Arthropod)

#######  Arachnid

[]{#arachnid}

Concept: [`arachnid`](https://w3id.org/isample/vocabulary/biologicentity/0.9/arachnid)

Child of:
 [`arthropod`](#arthropod)

a group of arthropods that share several key characteristics,
including two main body segments, four pairs of legs, lack of
antennae, simple eyes, and specialized feeding and defense structures
called chelicerae (ChatGPT)

#######  Crustaceans

[]{#crustacea}

Concept: [`crustacea`](https://w3id.org/isample/vocabulary/biologicentity/0.9/crustacea)

Child of:
 [`arthropod`](#arthropod)

arthropod taxon which includes such animals as decapods, seed shrimp,
branchiopods, fish lice, krill, remipedes, isopods, barnacles,
copepods, amphipods and mantis shrimp.  crustaceans have an
exoskeleton, which they moult to grow. They are distinguished from
other groups of arthropods, such as insects, myriapods and
chelicerates, by the possession of biramous (two-parted) limbs, and by
their larval forms, such as the nauplius stage of branchiopods and
copepods. (https://en.wikipedia.org/wiki/Crustacean)

#######  Insect

[]{#hexapoda}

Concept: [`hexapoda`](https://w3id.org/isample/vocabulary/biologicentity/0.9/hexapoda)

Child of:
 [`arthropod`](#arthropod)

Include all hexapoda here; Insects are a group of hexapod arthropods
characterized by having three main body segments (head, thorax, and
abdomen), six legs, and wings in many species. All other hexapod
arthropods, such as springtails and diplurans, are not classified as
insects, but they share the same body plan of three main body segments
and six legs. However, they lack wings and other features that are
unique to insects. Therefore, all insects are hexapods, but not all
hexapods are insects. (ChatGPT)

#######  Myriapod

[]{#myriapod}

Concept: [`myriapod`](https://w3id.org/isample/vocabulary/biologicentity/0.9/myriapod)

Child of:
 [`arthropod`](#arthropod)

Arthropods such as millipedes and centipedes.
(https://en.wikipedia.org/wiki/Myriapoda). A group of arthropods that
have long, segmented body with numerous pairs of legs, simple eyes,
specialized mouthparts, and a primarily terrestrial habitat, which
distinguishes them from other arthropod groups such as insects and
crustaceans. (ChatGPT)

#######  Other arthropod

[]{#otherarthropod}

Concept: [`otherarthropod`](https://w3id.org/isample/vocabulary/biologicentity/0.9/otherarthropod)

Child of:
 [`arthropod`](#arthropod)

includes Chelicerata (horseshoe crabs, scorpions, and sea spiders),
Trilobitomorpha ( extinct trilobites), and  Pentastomida (parasitic
arthropods that infect the respiratory systems of reptiles and
mammals). (ChatGPT)

######  Mollusca

[]{#mollusca}

Concept: [`mollusca`](https://w3id.org/isample/vocabulary/biologicentity/0.9/mollusca)

Child of:
 [`Animalia`](#Animalia)

animals that have a soft body with a mantle, a radula (ribbon-like
structure covered in tiny teeth that is used to scrape food), a
muscular foot, an open circulatory system, and a visceral mass that
contains the internal organs, including the digestive, excretory, and
reproductive systems. (ChatGPT)

######  Other invertebrate

[]{#otherinvertebrate}

Concept: [`otherinvertebrate`](https://w3id.org/isample/vocabulary/biologicentity/0.9/otherinvertebrate)

Child of:
 [`Animalia`](#Animalia)

Includes Cnidaria (jellyfish, coral, anemones), Echinodermata
(starfish, sea urchins, sea cucumbers), Nematoda (roundworms),
Platyhelminthes (flatworms), Annelida (segmented worms), Ctenophora
(comb jellies), Brachiopoda (lamp shells), Bryozoa (moss animals),
Chaetognatha (arrow worms), Hemichordata (acorn worms),
Xenacoelomorpha (simple-bodied worms) (ChatGPT)

######  Porifera

[]{#porifera}

Concept: [`porifera`](https://w3id.org/isample/vocabulary/biologicentity/0.9/porifera)

Child of:
 [`Animalia`](#Animalia)

multicellular animals that have bodies full of pores and channels
allowing water to circulate through them, consisting of jelly-like
mesohyl sandwiched between two thin layers of cells.
(https://en.wikipedia.org/wiki/Sponge)

#####  Fungi

[]{#fungi}

Concept: [`Fungi`](https://w3id.org/isample/vocabulary/biologicentity/0.9/Fungi)

Child of:
 [`eukaryote`](#eukaryote)

eukaryotic organisms that contain chitin in their cell walls, are
heterotrophs (they obtain their nutrients by absorbing organic
material from their environment, either as decomposers, parasites, or
symbionts) , lack chloroplasts, reproduce both sexually and asexually,
and can take on a variety of growth forms, including single-celled
yeasts, multicellular molds, and complex, specialized fruiting bodies.
(ChatGPT)

######  Macrofungi

[]{#macrofungi}

Concept: [`macrofungi`](https://w3id.org/isample/vocabulary/biologicentity/0.9/macrofungi)

Child of:
 [`Fungi`](#Fungi)

Macrofungi refers to all fungi that produce visible fruiting bodies.
These fungi are evolutionarily and ecologically very divergent.
Evolutionarily, they belong to two main phyla, Ascomycota and
Basidiomycota, and many of them have relatives that cannot form
visible fruiting
bodies.(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6106070/)

######  Microfungi

[]{#microfungi}

Concept: [`microfungi`](https://w3id.org/isample/vocabulary/biologicentity/0.9/microfungi)

Child of:
 [`Fungi`](#Fungi)

Microfungi or micromycetes are fungi—eukaryotic organisms such as
molds, mildews and rusts—which have microscopic spore-producing
structures. They exhibit tube tip-growth and have cell walls composed
of chitin, a polymer of N-acetylglucosamine. Microfungi are a
paraphyletic group, distinguished from macrofungi only by the absence
of a large, multicellular fruiting body. Include moulds, yeasts.
(https://en.wikipedia.org/wiki/Microfungi)

#####  Plantae

[]{#plantae}

Concept: [`Plantae`](https://w3id.org/isample/vocabulary/biologicentity/0.9/Plantae)

Child of:
 [`eukaryote`](#eukaryote)

Plants are eukaryotes that have cell walls made of cellulose,
specialized organelles called chloroplasts, which contain chlorophyll
and other pigments that allow plants to perform photosynthesis and
produce their own food;  a unique life cycle that involves alternating
between a haploid gametophyte stage and a diploid sporophyte stage;
specialized regions called apical meristems at the tips of their roots
and shoots, which allow for growth and the development of new tissues;
specialized structures for reproduction, including flowers, cones, and
spores, and most plants have specialized tissues called xylem and
phloem, which transport water, nutrients, and other substances
throughout the plant. (ChatGPT)

######  Bryophyte

[]{#bryophyte}

Concept: [`bryophyte`](https://w3id.org/isample/vocabulary/biologicentity/0.9/bryophyte)

Child of:
 [`Plantae`](#Plantae)

Non-vascular plants that do not have specialized tissues for
transporting water and nutrients;  includes mosses, Marchantiophyta
(liverworts), and Anthocerotophyta (hornworts). (ChatGPT)

######  Other plant

[]{#otherplant}

Concept: [`otherplant`](https://w3id.org/isample/vocabulary/biologicentity/0.9/otherplant)

Child of:
 [`Plantae`](#Plantae)

plants that do not fit in other plant sub class. Includes
Lycopodiophyta (clubmosses) and Equisetophyta (horsetails)

######  Pteridophyte

[]{#pteridophyte}

Concept: [`pteridophyte`](https://w3id.org/isample/vocabulary/biologicentity/0.9/pteridophyte)

Child of:
 [`Plantae`](#Plantae)

a vascular plant (with xylem and phloem) that disperses spores; they
produce neither flowers nor seeds, Includes  Ferns, horsetails (often
treated as ferns), and lycophytes (clubmosses, spikemosses, and
quillworts)

######  Seed plant

[]{#spermatophyte}

Concept: [`spermatophyte`](https://w3id.org/isample/vocabulary/biologicentity/0.9/spermatophyte)

Child of:
 [`Plantae`](#Plantae)

Plant that produces seeds, hence the alternative name seed plant.
Spermatophytes are a subset of the embryophytes or land plants. They
include most familiar types of plants, including all flowers and most
trees, but exclude some other types of plants such as ferns, mosses,
algae. (https://en.wikipedia.org/wiki/Spermatophyte). Includes
Gymnosperms (naked-seed plants) and Angiosperms (flowering plants).

#####  Protista

[]{#protista}

Concept: [`Protista`](https://w3id.org/isample/vocabulary/biologicentity/0.9/Protista)

Child of:
 [`eukaryote`](#eukaryote)

any organism whose cells contain a cell nucleus (a eucaryote) that is
not an animal, plant, or fungus.
(https://en.wikipedia.org/wiki/Protist).  Protista is not a specific
taxonomic group, but a term that historically referred to a group of
eukaryotic organisms that did not fit into the other kingdoms of
plants, animals, and fungi. (ChatGPT)

######  Amoebozoa

[]{#amoebozoa}

Concept: [`amoebozoa`](https://w3id.org/isample/vocabulary/biologicentity/0.9/amoebozoa)

Child of:
 [`Protista`](#Protista)

a diverse group of organisms that share certain characteristics, such
as the ability to move using pseudopodia, temporary extensions of the
cell membrane and cytoplasm that allow the cell to crawl or engulf
food particles, the lack of rigid cell walls, presence of
mitochondria, which are organelles that generate energy for the cell
through cellular respiration (chatGPT)

#######  Myxomycetes

[]{#myxomycete}

Concept: [`myxomycete`](https://w3id.org/isample/vocabulary/biologicentity/0.9/myxomycete)

Child of:
 [`amoebozoa`](#amoebozoa)

Aclass of slime molds. All species pass through several, very
different morphologic phases, such as microscopic individual cells,
slimy amorphous organisms visible with the naked eye and conspicuously
shaped fruit bodies. Although they are monocellular, they can reach
immense widths and weights. Some consider the Myxomycota to be a
separate kingdom, with an unsettled phylogeny because of conflicting
molecular and developmental data. The relations among Myxogastrid
orders are as yet unclear. (https://en.wikipedia.org/wiki/Mycetozoa).
Mycetozoa includes the slime molds, which are a group of organisms
that have both amoeboid and fungal-like characteristics. The Mycetozoa
can be further subdivided into two groups: the plasmodial slime molds
and the cellular slime molds. Myxomycetes are unique among the
Amoebozoa in that they have a complex life cycle involving the
formation of spore-bearing structures called fruiting bodies, which is
a key feature that distinguishes them from other amoebae. (ChatGPT)

######  Protozoa

[]{#protozoa}

Concept: [`protozoa`](https://w3id.org/isample/vocabulary/biologicentity/0.9/protozoa)

Child of:
 [`Protista`](#Protista)

A single-celled eukaryote, either free-living or parasitic, that feed
on organic matter such as other microorganisms or organic tissues and
debris. Historically, protozoans were regarded as 'one-celled
animals', because they often possess animal-like behaviours, such as
motility and predation, and lack a cell wall, as found in plants and
many algae. (https://en.wikipedia.org/wiki/Protozoa)

#####  Algae

[]{#algae}

Concept: [`algae`](https://w3id.org/isample/vocabulary/biologicentity/0.9/algae)

Child of:
 [`eukaryote`](#eukaryote)

informal term for a large and diverse group of photosynthetic
eukaryotic organisms.  Included organisms range from unicellular
microalgae, such as Chlorella, Prototheca and the diatoms, to
multicellular forms, such as the giant kelp, a large brown alga which
may grow up to 50 metres (160 ft) in length. Most are aquatic and
autotrophic (they generate food internally) and lack many of the
distinct cell and tissue types, such as stomata, xylem and phloem that
are found in land plants.  Includes red algae (Rhodophycophyta), brown
algae (Phaeophycophyta), and green algae (Chlorophycophyta).
https://en.wikipedia.org/wiki/Algae

#####  Eukaryotic microorganisms

[]{#eukaryoticmicroorganisms}

Concept: [`eukaryoticmicroorganisms`](https://w3id.org/isample/vocabulary/biologicentity/0.9/eukaryoticmicroorganisms)

Child of:
 [`eukaryote`](#eukaryote)

Eukaryote single-cell organisms that does not fit in one of the other
classes.

####  Lichen

[]{#lichen}

Concept: [`lichen`](https://w3id.org/isample/vocabulary/biologicentity/0.9/lichen)

Child of:
 [`biologicalentity`](#biologicalentity)

A composite organism that arises from algae or cyanobacteria living
among filaments of multiple fungi species in a mutualistic
relationship. (https://en.wikipedia.org/wiki/Lichen). Lichens are not
classified under a specific kingdom as they are a symbiotic
association between a fungus and either an alga or a cyanobacterium.
The fungal partner belongs to the kingdom Fungi, while the algal or
cyanobacterial partner belongs to either the kingdom Plantae or the
kingdom Bacteria, respectively. (ChatGPT)

####  Plasmid

[]{#plasmid}

Concept: [`plasmid`](https://w3id.org/isample/vocabulary/biologicentity/0.9/plasmid)

Child of:
 [`biologicalentity`](#biologicalentity)

A plasmid is a small, extrachromosomal DNA molecule within a cell that
is physically separated from chromosomal DNA and can replicate
independently. While chromosomes are large and contain all the
essential genetic information for living under normal conditions,
plasmids are usually very small and contain only additional genes that
may be useful in certain situations or conditions.
(https://en.wikipedia.org/wiki/Plasmid)

####  Prokaryote

[]{#prokaryote}

Concept: [`prokaryote`](https://w3id.org/isample/vocabulary/biologicentity/0.9/prokaryote)

Child of:
 [`biologicalentity`](#biologicalentity)

single-celled organisms that lack a nucleus and other membrane-bound
organelles. Unlike cells of animals and other eukaryotes, bacterial
cells do not contain a nucleus and rarely harbour membrane-bound
organelles. Molecular systematics showed prokaryotic life to consist
of two separate domains, originally called Eubacteria and
Archaebacteria, but now called Bacteria and Archaea that evolved
independently from an ancient common ancestor. Almost all prokaryotes
have a cell wall, a protective structure that allows them to survive
in extreme conditions, which is located outside of their plasma
membrane. Archaea and bacteria cannot reproduce sexually.

#####  Archaea

[]{#archaea}

Concept: [`archaea`](https://w3id.org/isample/vocabulary/biologicentity/0.9/archaea)

Child of:
 [`prokaryote`](#prokaryote)

archaeal cell walls are composed of polysaccharides (sugars). they
never have peptidoglycan in their cell walls, their cell membranes
contain lipids of unique composition (glycerol molecules are mirror
images of those found in other cells, and form ether linkages to
isoprenoid side chains), and their 16S ribosomal- RNA nucleotide
sequences are unlike those of bacteria.
(https://quizlet.com/234154298/archaea-and-bacteria-flash-cards/).
The common characteristics of Archaebacteria known to date are these:
(1) the presence of characteristic tRNAs and ribosomal RNAs; (2) the
absence of peptidoglycan cell walls, with in many cases, replacement
by a largely proteinaceous coat; (3) the occurrence of ether linked
lipids built from phytanyl chains and (4) in all cases known so far,
their occurrence only in unusual habitats.
(https://pubmed.ncbi.nlm.nih.gov/691075/)

#####  Bacteria

[]{#bacteria}

Concept: [`bacteria`](https://w3id.org/isample/vocabulary/biologicentity/0.9/bacteria)

Child of:
 [`prokaryote`](#prokaryote)

a large domain of prokaryotic microorganisms. Bacterial cells do not
contain a nucleus and rarely harbour membrane-bound organelles.  The
bacterial cell is surrounded by a cell membrane, which is made
primarily of phospholipids. This membrane encloses the contents of the
cell and acts as a barrier to hold nutrients, proteins and other
essential components of the cytoplasm within the cell.  Bacterial cell
walls are composed of peptidoglycan, a complex of protein and sugars,
while archaeal cell walls are composed of polysaccharides (sugars).
(https://en.wikipedia.org/wiki/Bacteria)

####  Virus

[]{#virus}

Concept: [`virus`](https://w3id.org/isample/vocabulary/biologicentity/0.9/virus)

Child of:
 [`biologicalentity`](#biologicalentity)

A virus is a submicroscopic infectious agent that replicates only
inside the living cells of an organism. Realms are Adnaviria,
Duplodnaviria, Monodnaviria, Riboviria, Ribozyviria, Varidnaviria
(https://en.wikipedia.org/wiki/Virus). Viruses are not cells at all,
so they are neither prokaryotes nor eukaryotes. (https://bio.libretext
s.org/Bookshelves/Introductory_and_General_Biology/Book)

#####  Other Virus

[]{#othervirus}

Concept: [`othervirus`](https://w3id.org/isample/vocabulary/biologicentity/0.9/othervirus)

Child of:
 [`virus`](#virus)

Virus that is not a member of order Caudovirales (e.g., bacteriophage
T4, lambda phage).

#####  Phage

[]{#phage}

Concept: [`phage`](https://w3id.org/isample/vocabulary/biologicentity/0.9/phage)

Child of:
 [`virus`](#virus)

A bacteriophage, also known informally as a phage, is a duplodnaviria
virus that infects and replicates within bacteria and archaea.
Bacteriophages are composed of proteins that encapsulate a DNA or RNA
genome, and may have structures that are either simple or elaborate.
Their genomes may encode as few as four genes (e.g. MS2) and as many
as hundreds of genes. Phages replicate within the bacterium following
the injection of their genome into its cytoplasm.
(https://en.wikipedia.org/wiki/Bacteriophage).  Includes all virus in
order Caudovirales (e.g., bacteriophage T4, lambda phage).

###  Earth environment

[]{#earthenvironment}

Concept: [`earthenvironment`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/earthenvironment)

Child of:
 [`anysampledfeature`](#anysampledfeature)

specimen samples the natural earth environment

See Also:

* [<http://purl.bioontology.org/ontology/MESH/D004777>](http://purl.bioontology.org/ontology/MESH/D004777)
* [<http://semanticscience.org/resource/SIO_000955>](http://semanticscience.org/resource/SIO_000955)

####  Atmosphere

[]{#atmosphere}

Concept: [`atmosphere`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/atmosphere)

Child of:
 [`earthenvironment`](#earthenvironment)

specimen samples the Earth's atmosphere

See Also:

* [<http://purl.obolibrary.org/obo/ENVO_01000267>](http://purl.obolibrary.org/obo/ENVO_01000267)
* [<http://purl.obolibrary.org/obo/RBO_00000018>](http://purl.obolibrary.org/obo/RBO_00000018)

####  Earth interior

[]{#earthinterior}

Concept: [`earthinterior`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/earthinterior)

Child of:
 [`earthenvironment`](#earthenvironment)

Specimen samples solid material within the earth (fluids in pore space
in earth interior sample 'subsurface fluid reservoir'

####  Earth surface

[]{#earthsurface}

Concept: [`earthsurface`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/earthsurface)

Child of:
 [`earthenvironment`](#earthenvironment)

Specimen samples the interface between solid earth and hydrosphere or
atmosphere. Includes samples representing things collected on the
surface, or in the uppermost part of the material below the surface.
Not including recently deposited sediment that has not been modified
by interaction with the surface environment.

#####  Lake river or stream bottom

[]{#lakeriverstreambottom}

Concept: [`lakeriverstreambottom`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/lakeriverstreambottom)

Child of:
 [`earthsurface`](#earthsurface)

Specimen samples the solid Earth interface with a lake or flowing
water body

#####  Marine water body bottom

[]{#marinewaterbodybottom}

Concept: [`marinewaterbodybottom`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/marinewaterbodybottom)

Child of:
 [`earthsurface`](#earthsurface)

Specimen samples the solid Earth interface with marine or brackish
water body. Includes benthic boundary layer:  the bottom layer of
water and the uppermost layer of sediment directly influenced by the
overlying water

#####  Subaerial surface environment

[]{#subaerialsurfaceenvironment}

Concept: [`subaerialsurfaceenvironment`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/subaerialsurfaceenvironment)

Child of:
 [`earthsurface`](#earthsurface)

Specimen samples the  interface between solid Earth and atmosphere.
Sample is collected on the surface, or immediately below surface (zone
of bioturbation). Include soil and recently deposited subaerial
sediment at the surface.

####  Glacier environment

[]{#glacierenvironment}

Concept: [`glacierenvironment`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/glacierenvironment)

Child of:
 [`earthenvironment`](#earthenvironment)

Sample of ice, water, or other thing from a glacier, ice sheet, ice
shelf, iceberg. Does not include various environments adjacent to
glacier.

####  Subsurface fluid reservoir

[]{#subsurfacefluidreservoir}

Concept: [`subsurfacefluidreservoir`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/subsurfacefluidreservoir)

Child of:
 [`earthenvironment`](#earthenvironment)

Specimen samples fluid that resides in fractures or intergranular
porosity in the solid earth.

####  Water body

[]{#waterbody}

Concept: [`waterbody`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/waterbody)

Child of:
 [`earthenvironment`](#earthenvironment)

specimen samples the hydrosphere

#####  Marine environment

[]{#marinewaterbody}

Concept: [`marinewaterbody`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/marinewaterbody)

Child of:
 [`waterbody`](#waterbody)

specimen samples marine hydrosphere

See Also:

* [<http://purl.obolibrary.org/obo/ENVO_01000686>](http://purl.obolibrary.org/obo/ENVO_01000686)

#####  Terrestrial water body

[]{#terrestrialwaterbody}

Concept: [`terrestrialwaterbody`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/terrestrialwaterbody)

Child of:
 [`waterbody`](#waterbody)

specimen samples terrestrial hydrosphere-- lake, other standing water,
or a flowing water body (river, stream..) Include saline water in
terrestrial evaporite environments.

###  Extraterrestrial environment

[]{#extraterrestrialenvironment}

Concept: [`extraterrestrialenvironment`](https://w3id.org/isample/vocabulary/sampledfeature/0.9/extraterrestrialenvironment)

Child of:
 [`anysampledfeature`](#anysampledfeature)

specimen samples environment outside of solid earth, hydrosphere, or
atmosphere.


