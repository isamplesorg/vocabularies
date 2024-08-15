---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 4
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#iSamplesMaterialSampleObjectTypeVocabulary}

# **Concept scheme:** iSamples Material Sample Object Type Vocabulary

Vocabulary last modified:  2024-04-19

subtitle: 
  Broad categories to specify the kind of physical object identified as the ‘sample’.

Namespace: 
[`https://w3id.org/isample/vocabulary/materialsampleobjecttype/1.0/conceptscheme`](https://w3id.org/isample/vocabulary/materialsampleobjecttype/1.0/conceptscheme)

**History**

* 2022-01-07 SMR Change base URI to https://w3id.org/isample/vocabulary/, setting up resolution using w3id. Make the conceptScheme and ontology. Add Dublin core imports.
* 2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes in definitions. Add skos matches to URIs from other vocabularies.
* 2022-09-30 SMR per https://github.com/isamplesorg/metadata/issues/109, change specimen to sample in vocabulary names and labels. Add 'Slurry biome aggregation' and 'Bundle biome aggregation' (github issue 110). Rename 'liquid or gas' sample type to 'fluid in container' (github issue 108).
* 2023-07-27 SMR modify base specimen type vocabulary, add 'Non biologic solid object'  change broader relations in this vocab to use that as parent class where appropriate.  Intention is a specimen category for solid objects that are not biologic; this subsumes 'Fossil' and 'Artifact', but excludes living organism, their parts and products. Obviously there is some overlap with Research specimens.
* 2023-11-06 SMR add missing inScheme on Non-biologic solid object and solid materal specimen. Update version number in URI to 1.0
* 2024-04-19 SMR update language to always use 'material sample' instead of specimen or physical specimen, including in text, labels, and in the URI tokens.  Edit defintions to improve clarity.

- [Material sample](#materialsample)
    - [Any aggregation material sample](#anyaggregation)
        - [Anthropogenic aggregation](#anthropogenicaggregation)
        - [Biome aggregation sample](#biomeaggregation)
            - [Bundle biome aggregation](#bundlebiomeaggregation)
            - [Slurry biome aggregation](#slurrybiomeaggregation)
        - [Aggregation](#genericaggregation)
    - [Biological material sample](#biologicalmaterialsample)
        - [Biome aggregation sample](#biomeaggregation)
            - [Bundle biome aggregation](#bundlebiomeaggregation)
            - [Slurry biome aggregation](#slurrybiomeaggregation)
        - [Organism part](#organismpart)
        - [Organism product](#organismproduct)
        - [Whole organism material sample](#wholeorganism)
    - [Fluid in container](#fluidincontainer)
    - [Non biologic solid object](#nonbiologicsolidobject)
        - [Artifact](#artifact)
        - [Fossil](#fossil)
        - [Other solid object](#othersolidobject)
        - [Solid material sample](#solidmaterialsample)
    - [Research product](#researchproduct)
        - [Analytical preparation](#analyticalpreparation)
        - [Experiment product](#experimentalproduct)

**Concepts**

[]{#materialsample}

##  Material sample


- A material entity that represents an entity of interest in whole or
in part (http://rs.tdwg.org/dwc/terms/MaterialSample). Top concept in
material sample object type hierarchy.  Represents any material sample
object.

- **Alternate labels:**
Physical specimen

- Concept URI token: materialsample


[]{#anyaggregation}

###  Any aggregation material sample


- Child of:
 [`materialsample`](#materialsample)

- Sample consists of a bunch of material fragments, not related to the
same object (e.g. not a bunch of broken pot sherds that might be
reassembled), but taken together representative of the sampled
feature. Examples: loose soil, sediment, crushed rock,  particulate,
bunches of unrelated pot sherd, human production waste, filtrates and
residues. The sample requires some kind of container to keep it
together. Cores of loosely consolidated material are considered 'Solid
material specimen' when preserved such that the internal parts have
spatial relationships (e.g. upper part, lower part, sedimentary
structures).
- Concept URI token: anyaggregation


[]{#anthropogenicaggregation}

####  Anthropogenic aggregation


- Child of:
 [`anyaggregation`](#anyaggregation)

- An aggregate material sample consisting of fragments of material
produced by human activity, not described individually, and generally
not all originating from the same object.  Includes pottery in an
excavation unit that gets an aggregate description, production waste,
production raw-materials, or other residues (broken bits of plaster
from a destroyed wall), synthetic powders.
- Concept URI token: anthropogenicaggregation


[]{#biomeaggregation}

####  Biome aggregation sample


- Child of:
 [`anyaggregation`](#anyaggregation)
 [`biologicalmaterialsample`](#biologicalmaterialsample)

- Material sample that is an aggregation of whole or fragmentary parts
of multiple organisms, microscopic or megascopic, representative of
some sampled feature.
- Concept URI token: biomeaggregation


[]{#bundlebiomeaggregation}

#####  Bundle biome aggregation


- Child of:
 [`biomeaggregation`](#biomeaggregation)

- Material sample that is an aggregation of whole organisms
representative of some biome.
- Concept URI token: bundlebiomeaggregation


[]{#slurrybiomeaggregation}

#####  Slurry biome aggregation


- Child of:
 [`biomeaggregation`](#biomeaggregation)

- Material sample that consists of mixed organic and inorganic
material, including whole organisms and organism fragments.
- Concept URI token: slurrybiomeaggregation


[]{#genericaggregation}

####  Aggregation


- Child of:
 [`anyaggregation`](#anyaggregation)

- An aggregate material sample that is not biogenic or composed of
anthropogenic material fragments.  Examples: loose soil or sediment
(e.g. in a bag), rock chips, particulate filtrate or precipitate; rock
powders.
- Concept URI token: genericaggregation


[]{#biologicalmaterialsample}

###  Biological material sample


- Child of:
 [`materialsample`](#materialsample)

- Material sample representative of one or more living organisms from
a particular biome context, megascopic or microscopic
- Concept URI token: biologicalmaterialsample


[]{#biomeaggregation}

####  Biome aggregation sample


- Child of:
 [`anyaggregation`](#anyaggregation)
 [`biologicalmaterialsample`](#biologicalmaterialsample)

- Material sample that is an aggregation of whole or fragmentary parts
of multiple organisms, microscopic or megascopic, representative of
some sampled feature.
- Concept URI token: biomeaggregation


[]{#bundlebiomeaggregation}

#####  Bundle biome aggregation


- Child of:
 [`biomeaggregation`](#biomeaggregation)

- Material sample that is an aggregation of whole organisms
representative of some biome.
- Concept URI token: bundlebiomeaggregation


[]{#slurrybiomeaggregation}

#####  Slurry biome aggregation


- Child of:
 [`biomeaggregation`](#biomeaggregation)

- Material sample that consists of mixed organic and inorganic
material, including whole organisms and organism fragments.
- Concept URI token: slurrybiomeaggregation


[]{#organismpart}

####  Organism part


- Child of:
 [`biologicalmaterialsample`](#biologicalmaterialsample)

- Material sample that is part of an organism, e.g. a tissue sample,
plant leaf, flower, bird feather. Include internal parts not composed
of organic material (e.g. teeth, bone), and hard body parts that are
not shed (hoof, horn, tusk, claw).  Hair is tricky, include here for
now.  Does not necessarily imply existance of parent sample. Not
fossilized; generally includes organism parts native to deposits of
Holocene to Recent age.
- Concept URI token: organismpart


[]{#organismproduct}

####  Organism product


- Child of:
 [`biologicalmaterialsample`](#biologicalmaterialsample)

- Material sample is a thing produced by some organism, generally not
composed of organic material or including biological tissue, e.g.
Shell, antler, egg shell, coral skeleton (organic tissue not
included), fecal matter, cocoon, web.  Consider internal parts not
composed of organic material (e.g. teeth, bone) and hard body parts
that are not shed (hoof, horn, tusk) to be organism parts.
- Concept URI token: organismproduct


[]{#wholeorganism}

####  Whole organism material sample


- Child of:
 [`biologicalmaterialsample`](#biologicalmaterialsample)

- Material sample consists of the bodies of one or more entire
organisms of the same species, from any kingdom.
- Concept URI token: wholeorganism


[]{#fluidincontainer}

###  Fluid in container


- Child of:
 [`materialsample`](#materialsample)

- Material sample is a liquid, gas, or mixed dominantly fluid phase
material that is necessarily inside some container. Fluids might
include minor solid particles. The container is typically human made,
but also includes natural fluid containers, e.g. a fluid inclusion in
a mineral grain.  Fluids might be colloids, foams, gels, or
suspensions. The sample is the fluid substance; fluid samples
collected to analyze the contained biome should be considered 'Biome
aggregation sample'
- Concept URI token: fluidincontainer


[]{#nonbiologicsolidobject}

###  Non biologic solid object


- Child of:
 [`materialsample`](#materialsample)

- Individual solid object, the substance of which is not formed
directly by or part of a living organism
- Concept URI token: nonbiologicsolidobject


[]{#artifact}

####  Artifact


- Child of:
 [`nonbiologicsolidobject`](#nonbiologicsolidobject)

- An object made (manufactured, shaped, modified) by a human being, or
precursor hominid. Include a set of pieces belonging originally to a
single object and treated as a single sample.
- Concept URI token: artifact


[]{#fossil}

####  Fossil


- Child of:
 [`nonbiologicsolidobject`](#nonbiologicsolidobject)

- Material sample is the remains or trace of one or more organisms
preserved in rock; includes whole body, body parts (usually bone or
shell), and trace fossils. An organism or organism part becomes a
fossil when it has undergone some fossilization process that entails
physical and chemical changes akin to diagenesis in a sedimentary
rock. Includes trace fossils, which are manifestations of biologic
activity preserved in a rock body (typically sedimentary), without
included preserved body parts.
- Concept URI token: fossil


[]{#othersolidobject}

####  Other solid object


- Child of:
 [`nonbiologicsolidobject`](#nonbiologicsolidobject)

- A non-biologic solid object that is not one of the other types.
- Concept URI token: othersolidobject


[]{#solidmaterialsample}

####  Solid material sample


- Child of:
 [`nonbiologicsolidobject`](#nonbiologicsolidobject)

- Individual solid object, not formed directly by or part of a living
organism, that is intended to be representative of some material.
- Concept URI token: solidmaterialsample


[]{#researchproduct}

###  Research product


- Child of:
 [`materialsample`](#materialsample)

- Material sample is a product of some research workflow, e.g. a thin
section, an XRF pellet, a grain mount, SEM stub, synthetic rock or
mineral ...  In general there should be a link to a parent material
sample from which this was derived.  Might be aggregation (e.g. a
synthetic material powder) or a solid object.
- Concept URI token: researchproduct


[]{#analyticalpreparation}

####  Analytical preparation


- Child of:
 [`researchproduct`](#researchproduct)

- Material sample is a product of processing required for some
observation procedure, e.g. thin section, XRF bead, SEM stub, rock
powder. If identified separately, this should have a ‘parent’ link to
the original sample
- Concept URI token: analyticalpreparation


[]{#experimentalproduct}

####  Experiment product


- Child of:
 [`researchproduct`](#researchproduct)

- Material sample that is the product of an experimental procedure
(e.g. synthetic material)
- Concept URI token: experimentalproduct



