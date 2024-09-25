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

[]{#iSamplesMaterialsVocabulary}

# **Concept scheme:** iSamples Materials Vocabulary 

Vocabulary last modified:  2024-08-14

subtitle: 
  High level vocabulary to specify the kind of material that constitutes a physical sample

Namespace: 
[`https://w3id.org/isample/vocabulary/material/materialsvocabulary`](https://w3id.org/isample/vocabulary/material/materialsvocabulary)

**History**

* 2022-01-05 SMR version 0.9, change base uri to https://w3id.org/isample/vocabulary/material/0.9/ for testing with ESIP COR and w3id uri resolution
* 2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes to some definitions.  Add skos matches to URIs from other vocabularies; 2023-11-05 version 1.0, in preparation for release. 
* 2024-08-14 SMR, various updates since 2023-12:  change seeAlso to closeMatch for Rock mapping to http://resource.geosciml.org/classifier/cgi/lithology/rock; minor edits to align with manuscript about the metadata schema; update vocabularies to use 'material sample' instead of 'specimen'; update schema.org namespace to http://; add provider and codeRepository in conceptScheme metadata; minor typo fixes and definition edits.

- [Material ](#material)
    - [Anthropogenic material](#anyanthropogenicmaterial)
        - [Anthropogenic metal material ](#anthropogenicmetal)
        - [Other anthropogenic material](#otheranthropogenicmaterial)
    - [Any ice](#anyice)
        - [Frozen water](#waterice)
    - [Biogenic non-organic material](#biogenicnonorganicmaterial)
    - [Dispersed media](#dispersedmedia)
    - [Natural Solid Material](#earthmaterial)
        - [Mineral ](#mineral)
        - [Mixed soil sediment or rock](#mixedsoilsedimentrock)
        - [Particulate](#particulate)
        - [Rock or sediment](#rockorsediment)
            - [Rock](#rock)
            - [Sediment](#sediment)
        - [Soil](#soil)
    - [Fluid material](#fluid)
        - [Gaseous material](#gas)
        - [Liquid water](#liquidwater)
        - [Non-aqueous liquid material ](#nonaqueousliquid)
    - [Organic material](#organicmaterial)

**Concepts**

[]{#material}

##  Material


- Top Concept in iSamples Material Category scheme
- Concept URI: https://w3id.org/isample/vocabulary/material/material


[]{#anyanthropogenicmaterial}

###  Anthropogenic material


- Child of:
 [`material`](#material)

- Material produced by human activity.
- Concept URI: https://w3id.org/isample/vocabulary/material/anyanthropogenicmaterial


[]{#anthropogenicmetal}

####  Anthropogenic metal material


- Child of:
 [`anyanthropogenicmaterial`](#anyanthropogenicmaterial)

- Metal that has been produced or used by humans. Samples of naturally
occurring metallic material (e.g. native copper, gold nuggets) should
be considered mineral material. Metallic material is material that
when polished or fractured, shows a lustrous appearance, and conducts
electricity and heat relatively well. Metals are typically malleable
(they can be hammered into thin sheets) or ductile (can be drawn into
wires). The boundaries between metals, nonmetals, and metalloids
fluctuate slightly due to a lack of universally accepted definitions
of the categories involved. (https://en.wikipedia.org/wiki/Metal, c.f.
http://purl.obolibrary.org/obo/ENVO_01001069)
- Concept URI: https://w3id.org/isample/vocabulary/material/anthropogenicmetal


[]{#otheranthropogenicmaterial}

####  Other anthropogenic material


- Child of:
 [`anyanthropogenicmaterial`](#anyanthropogenicmaterial)

- Non-metallic material produced by human activity. Organic products
of agricultural activity are both anthropogenic and organic. Include
lab preparations like XRF pellet and rock powders. Examples: ceramics,
concrete, slag, (anthropogenic) glass, mine tailing, plaster, waste.
- Concept URI: https://w3id.org/isample/vocabulary/material/otheranthropogenicmaterial


[]{#anyice}

###  Any ice


- Child of:
 [`material`](#material)

- a material that is in a solid state under the temperature and
pressure conditions of the preserved sample, but is a liquid or gas at
Standard Temperature and Pressure (STP).
- Concept URI: https://w3id.org/isample/vocabulary/material/anyice


[]{#waterice}

####  Frozen water


- Child of:
 [`anyice`](#anyice)

- Water that is in a solid state.

- **Alternate labels:**
Water ice

- Concept URI: https://w3id.org/isample/vocabulary/material/waterice


[]{#biogenicnonorganicmaterial}

###  Biogenic non-organic material


- Child of:
 [`material`](#material)

- Material produced by an organism but not composed of 'very large
molecules of biological origin.' E.g. bone, tooth, shell, coral
skeleton,
- Concept URI: https://w3id.org/isample/vocabulary/material/biogenicnonorganicmaterial


[]{#dispersedmedia}

###  Dispersed media


- Child of:
 [`material`](#material)

- Material that contains discrete elements of some material dispersed
in a continuous fluid medium.  The dispersed component can be a gas, a
liquid or a solid (based on
https://en.wikipedia.org/wiki/Dispersed_media). Does not include
mixtures of granular material like soil, sediment, particulate, or
solids that would be considered  rock material.
- Concept URI: https://w3id.org/isample/vocabulary/material/dispersedmedia


[]{#earthmaterial}

###  Natural Solid Material


- Child of:
 [`material`](#material)

- A naturally occurring solid material that is not anthropogenic,
biogenic, or ice.
- Concept URI: https://w3id.org/isample/vocabulary/material/earthmaterial


[]{#mineral}

####  Mineral


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material consists of a single mineral or mineraloid phase.  'A
mineral is an element or chemical compound that is normally
crystalline and that has been formed as a result of geological
processes.' (Nickel, Ernest H. (1995), The definition of a mineral,
The Canadian Mineralogist. 33 (3): 689–90). Include mineraloids. ... A
material primarily composed of some substance that is naturally
occurring, solid and stable at room temperature, representable by a
chemical formula, usually abiogenic, and that has an ordered atomic
structure. (http://purl.obolibrary.org/obo/ENVO_01000256). The
identity of a mineral species is defined by a crystal structure and a
chemical composition that might include various specific elemental
substitutions in that structure. Mineraloid: A naturally occurring
mineral-like substance that does not demonstrate crystallinity.
Mineraloids possess chemical compositions that vary beyond the
generally accepted ranges for specific minerals. Examples: obsidian,
Opal. (https://en.wikipedia.org/wiki/Mineraloid)
- Concept URI: https://w3id.org/isample/vocabulary/material/mineral


[]{#mixedsoilsedimentrock}

####  Mixed soil sediment or rock


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material is mixed aggregation of fragments of undifferentiated soil,
sediment or rock origin. e.g. cuttings from some boreholes (rock
fragments and caved soil or sediment).
- Concept URI: https://w3id.org/isample/vocabulary/material/mixedsoilsedimentrock


[]{#particulate}

####  Particulate


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material consists of microscopic particulate material derived by
precipitation, filtering, or settling from suspension in a fluid, e.g.
filtrate from water, deposition from atmosphere, astro material
particles. Might include mineral, organic, or biological material.
ENVO definition (ENVO_01000060) has "composed of microscopic portions
of solid or liquid material suspended in another environmental
material." Refine here to define as the solid particles, distinct from
a material in which they are suspended. A material that includes solid
or liquid particles suspended in another material would be a
dispersed_media in this scheme, not defined in ENVO. Human
manufactured particulates (e.g. rock powder) should be categorized as
'Anthropogenic material' as well as 'Particulate'
- Concept URI: https://w3id.org/isample/vocabulary/material/particulate


[]{#rockorsediment}

####  Rock or sediment


- Child of:
 [`earthmaterial`](#earthmaterial)

- Material is rock or sediment.  For example core from boreholes that
likely penetrate sediment near the surface and rock at greater depth,
with descriptions that do not clearly distinguish non-consolidated
sediment from rock.
- Concept URI: https://w3id.org/isample/vocabulary/material/rockorsediment


[]{#rock}

#####  Rock


- Child of:
 [`rockorsediment`](#rockorsediment)

- Consolidated aggregate of particles (grains) of rock, mineral
(including native elements), mineraloid, or solid organic material.
Includes mineral aggregates such as granite, shale, marble; natural
glass such as obsidian; organic material formed by geologic processes
such a coal;  extraterrestrial material in meteorites; and  crushed
rock fragments like drill cuttings from rock.  (based on
http://resource.geosciml.org/classifier/cgi/lithology/rock, same as
http://purl.obolibrary.org/obo/ENVO_00001995)
- Concept URI: https://w3id.org/isample/vocabulary/material/rock


[]{#sediment}

#####  Sediment


- Child of:
 [`rockorsediment`](#rockorsediment)

- Solid granular material transported by wind, water, or gravity, not
modified by interaction with biosphere or atmosphere (to differentiate
from soil). Particles might be derived by erosion of pre-existing
rock, from shell or other body parts from organisms, precipitated
chemically in the surficial environment, or generated by explosive
volcanic activity.
(http://resource.geosciml.org/classifier/cgi/lithology/sediment).
Sediment is not consolidated, i.e. the particulate constituents do not
adhere to each other strongly enough that the aggregate can be
considered a solid material in its own right. Similar to
http://purl.obolibrary.org/obo/ENVO_00002007
- Concept URI: https://w3id.org/isample/vocabulary/material/sediment


[]{#soil}

####  Soil


- Child of:
 [`earthmaterial`](#earthmaterial)

- Mixed granular mineral and organic matter modified by interaction
between earth material, biosphere, and atmosphere, consisting of
varying proportions of sand, silt, and clay, organic material such as
humus, gases, liquids, and a broad range of resident micro- and
macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of
horizons near the Earth's surface that, in contrast to the underlying
parent material, have been altered by the interactions of climate,
relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/
portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
(http://purl.obolibrary.org/obo/ENVO_00001998)

- See Also:
* [<http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280>](http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
- Concept URI: https://w3id.org/isample/vocabulary/material/soil


[]{#fluid}

###  Fluid material


- Child of:
 [`material`](#material)

- Substance that continually deforms (flows) under an applied shear
stress, or external force. Fluids are a phase of matter and include
liquids, gases and plasmas. They are substances with zero or small
shear modulus, and flow at a perceptible rate under any shear force
applied to them. (https://en.wikipedia.org/wiki/Fluid)
- Concept URI: https://w3id.org/isample/vocabulary/material/fluid


[]{#gas}

####  Gaseous material


- Child of:
 [`fluid`](#fluid)

- Material composed of one or more chemical entities that has neither
independent shape nor volume but tends to expand indefinitely
(http://purl.obolibrary.org/obo/ENVO_01000797). Infer that the sample
is curated in some kind of container.
- Concept URI: https://w3id.org/isample/vocabulary/material/gas


[]{#liquidwater}

####  Liquid water


- Child of:
 [`fluid`](#fluid)

- A material primarily composed of dihydrogen oxide in its liquid
form; infer that the sample is curated in some kind of container.
- Concept URI: https://w3id.org/isample/vocabulary/material/liquidwater


[]{#nonaqueousliquid}

####  Non-aqueous liquid material


- Child of:
 [`fluid`](#fluid)

- Liquid composed dominantly of material other than water. Includes
liquids that do not fit in any other category. E.g. alcohol,
petroleum.
- Concept URI: https://w3id.org/isample/vocabulary/material/nonaqueousliquid


[]{#organicmaterial}

###  Organic material


- Child of:
 [`material`](#material)

- Material derived from living organisms and composed primarily of one
or more very large molecules of biological origin. Examples: body
(animal or plant), body part, fecal matter, seeds, wood, tissue,
biological fluids, biological waste, algal material, biofilm,
necromass, plankton. source:
http://purl.obolibrary.org/obo/ENVO_01000155
- Concept URI: https://w3id.org/isample/vocabulary/material/organicmaterial



