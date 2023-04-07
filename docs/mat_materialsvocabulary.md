---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
title: "iSamples Materials Vocabulary"
date: "2023-04-07T07:26:25.797143+00:00"
subtitle: |
  High level vocabulary to specify the kind of material that constitutes a physical sample
execute:
  echo: false
---

Namespace: 
[`https://w3id.org/isample/vocabulary/material/0.9/materialsvocabulary`](https://w3id.org/isample/vocabulary/material/0.9/materialsvocabulary)

**History**

* 2022-01-05 SMR version 0.9, change base uri to https://w3id.org/isample/vocabulary/material/0.9/ for testing with ESIP COR and w3id uri resolution
* 2022-03-11 SMR change definitions from rdfs:comment to skos:definition. Minor fixes to some definitions.  Add skos matches to URIs from other vocabularies.

**Concepts**

- [Material ](#material)
    - [Any anthropogenic material](#anyanthropogenicmaterial)
        - [Anthropogenic metal material ](#anthropogenicmetal)
            - [brass](#brass)
            - [bronze](#bronze)
            - [Copper](#copper)
            - [Gold](#gold)
            - [iron](#iron)
            - [lead](#lead)
            - [pewter](#pewter)
        - [Anthropogenic material](#otheranthropogenicmaterial)
            - [Anthropogenic organic material](#anthropogenicorganicmaterial)
                - [Plastic (material)](#plastic)
            - [Ceramic clay](#ceramicclay)
                - [Brick clay](#brickclay)
                - [bucchero](#bucchero)
                - [faience](#faience)
                - [Porcelain](#porcelain)
                - [Terracotta](#terracotta)
                - [Terra sigilata](#terrasigilata)
            - [Fiber material](#fibermaterial)
            - [Glass](#glass)
            - [Paper](#paper)
            - [plaster](#plaster)
            - [Plaster or Mortar](#plasterormortar)
            - [Rubber](#rubber)
    - [Any ice](#anyice)
        - [Frozen water](#waterice)
    - [Biogenic non-organic material](#biogenicnonorganicmaterial)
        - [amber](#amber)
        - [bone](#bone)
        - [charcoal](#charcoal)
        - [coal](#coal)
        - [Shell](#shell)
    - [Dispersed media](#dispersedmedia)
    - [Natural Solid Material](#earthmaterial)
        - [Mineral ](#mineral)
            - [Hematite](#hematite)
            - [kaolin](#kaolin)
            - [mica](#mica)
            - [quartz](#quartz)
            - [Mineral-Borate](#boratemineral)
            - [Mineral-Carbonate or Nitrate](#carbonatenitratemineral)
            - [Mineral-Halide](#halidemineral)
            - [Mineral-Native Element](#nativeelementmineral)
            - [Mineral-Organic Compound](#organicmineral)
            - [Mineral-Oxide](#oxidemineral)
            - [Mineral-Phosphate, Arsenate, or Vanadate](#phosphatearsenatevanadatemineral)
            - [Mineral-Silicate or Germanate](#silicategermanatemineral)
            - [Mineral-Sulfate, Selenate, or Tellurate](#sulfateselenatetelluratemineral)
            - [Mineral-Sulfide or Sulfosalt](#sulfidesulfosaltmineral)
        - [Mixed soil sediment or rock](#mixedsoilsedimentrock)
        - [Particulate](#particulate)
            - [Cinder](#cinder)
        - [Rock or sediment](#rockorsediment)
            - [Rock](#rock)
                - [Basalt](#basalt)
                - [Chert](#chert)
                    - [flint](#flint)
                - [Cinder](#cinder)
                - [coal](#coal)
                - [dolomite](#dolomite)
                - [gabbro](#gabbro)
                - [greywacke](#greywacke)
                - [limestone](#limestone)
                - [marble](#marble)
                - [obsidian](#obsidian)
                - [pumice](#pumice)
                - [Slate](#slate)
                - [Travertine](#travertine)
                - [aphanite](#aphanite)
                - [breccia](#breccia)
                - [fault related material](#fault_related_material)
                    - [cataclasite series](#cataclasite_series)
                    - [mylonitic rock](#mylonitic_rock)
                    - [breccia gouge series](#breccia_gouge_series)
                - [fragmental igneous rock](#fragmental_igneous_rock)
                    - [pyroclastic rock](#pyroclastic_rock)
                - [igneous rock](#igneous_rock)
                    - [acidic igneous rock](#acidic_igneous_rock)
                        - [dacite](#dacite)
                        - [granitoid](#granitoid)
                            - [alkali feldspar granite](#alkali_feldspar_granite)
                            - [granite](#granite)
                            - [granodiorite](#granodiorite)
                            - [tonalite](#tonalite)
                        - [quartz rich igneous rock](#quartz_rich_igneous_rock)
                        - [rhyolitoid](#rhyolitoid)
                    - [basic igneous rock](#basic_igneous_rock)
                        - [basalt](#basalt)
                        - [gabbroic rock](#gabbroic_rock)
                    - [doleritic rock](#doleritic_rock)
                    - [exotic composition igneous rock](#exotic_composition_igneous_rock)
                    - [fine grained igneous rock](#fine_grained_igneous_rock)
                        - [andesite](#andesite)
                        - [basalt](#basalt)
                        - [dacite](#dacite)
                        - [foiditoid](#foiditoid)
                        - [high magnesium fine grained igneous rock](#high_magnesium_fine_grained_igneous_rock)
                        - [phonolitoid](#phonolitoid)
                        - [rhyolitoid](#rhyolitoid)
                        - [tephritoid](#tephritoid)
                        - [trachytoid](#trachytoid)
                    - [fragmental igneous rock](#fragmental_igneous_rock)
                        - [pyroclastic rock](#pyroclastic_rock)
                    - [glass rich igneous rock](#glass_rich_igneous_rock)
                    - [hypabyssal intrusive rock](#hypabyssal_intrusive_rock)
                    - [intermediate composition igneous rock](#intermediate_composition_igneous_rock)
                        - [andesite](#andesite)
                        - [dioritoid](#dioritoid)
                    - [phaneritic igneous rock](#phaneritic_igneous_rock)
                        - [anorthositic rock](#anorthositic_rock)
                        - [aplite](#aplite)
                        - [dioritoid](#dioritoid)
                        - [foid dioritoid](#foid_dioritoid)
                        - [foid gabbroid](#foid_gabbroid)
                        - [foid syenitoid](#foid_syenitoid)
                        - [foidolite](#foidolite)
                        - [gabbroid](#gabbroid)
                            - [gabbroic rock](#gabbroic_rock)
                            - [monzogabbroic rock](#monzogabbroic_rock)
                        - [granitoid](#granitoid)
                            - [alkali feldspar granite](#alkali_feldspar_granite)
                            - [granite](#granite)
                            - [granodiorite](#granodiorite)
                            - [tonalite](#tonalite)
                        - [hornblendite](#hornblendite)
                        - [pegmatite](#pegmatite)
                        - [peridotite](#peridotite)
                        - [pyroxenite](#pyroxenite)
                        - [quartz rich igneous rock](#quartz_rich_igneous_rock)
                        - [syenitoid](#syenitoid)
                    - [plutonic rock](#plutonic_igneous_rock)
                    - [porphyry](#porphyry)
                    - [ultrabasic igneous rock](#ultrabasic_igneous_rock)
                    - [ultramafic igneous rock](#ultramafic_igneous_rock)
                        - [hornblendite](#hornblendite)
                        - [peridotite](#peridotite)
                        - [pyroxenite](#pyroxenite)
                - [impact generated material](#impact_generated_material)
                - [Massive sulphide](#massive_sulphide)
                - [metamorphic rock](#metamorphic_rock)
                - [metasomatic rock](#metasomatic_rock)
                - [sedimentary rock](#sedimentary_rock)
                    - [carbonate sedimentary rock](#carbonate_sedimentary_rock)
                    - [clastic sedimentary rock](#clastic_sedimentary_rock)
                        - [diamictite](#diamictite)
                    - [generic conglomerate](#generic_conglomerate)
                    - [generic mudstone](#generic_mudstone)
                    - [generic sandstone](#generic_sandstone)
                    - [hybrid sedimentary rock](#hybrid_sedimentary_rock)
                    - [iron rich sedimentary rock](#iron_rich_sedimentary_rock)
                    - [non clastic siliceous sedimentary rock](#non_clastic_siliceous_sedimentary_rock)
                    - [organic rich sedimentary rock](#organic_rich_sedimentary_rock)
                        - [coal](#coal)
                    - [phosphorite](#phosphorite)
                - [tuffit](#tuffite)
                - [residual material](#residual_material)
            - [Sediment](#sediment)
                - [biogenic sediment](#biogenic_sediment)
                - [carbonate sediment](#carbonate_sediment)
                - [chemical sedimentary material](#chemical_sedimentary_material)
                - [clastic sediment](#clastic_sediment)
                    - [diamicton](#diamicton)
                - [gravel size sediment](#gravel_size_sediment)
                - [hybrid sediment](#hybrid_sediment)
                - [iron rich sediment](#iron_rich_sediment)
                - [mud size sediment](#mud_size_sediment)
                - [non clastic siliceous sediment](#non_clastic_siliceous_sediment)
                - [phosphate rich sediment](#phosphate_rich_sediment)
                - [sand size sediment](#sand_size_sediment)
                - [tephra](#tephra)
        - [Soil](#soil)
    - [Fluid material](#fluid)
        - [Gaseous material](#gas)
        - [Liquid water](#liquidwater)
        - [Non-aqueous liquid material ](#nonaqueousliquid)
    - [Organic material](#organicmaterial)
        - [Anthropogenic organic material](#anthropogenicorganicmaterial)
            - [Plastic (material)](#plastic)
        - [Organic animal product](#organicanimalproduct)
            - [Hair](#hair)
            - [Leather](#leather)
        - [Organic animal material](#organicanimalmaterial)
        - [Organic plant material](#organicplantmaterial)
            - [Wood](#wood)
        - [Plant Material](#plantmaterial)
            - [Plant fiber](#plantfiber)
            - [Wood](#wood)

##  Material

[]{#material}

Concept: [`material`](https://w3id.org/isample/vocabulary/material/0.9/material)

Top Concept in iSamples Material Category scheme

###  Any anthropogenic material

[]{#anyanthropogenicmaterial}

Concept: [`anyanthropogenicmaterial`](https://w3id.org/isample/vocabulary/material/0.9/anyanthropogenicmaterial)

Child of:
 [`material`](#material)

Material produced by human activity.

####  Anthropogenic metal material

[]{#anthropogenicmetal}

Concept: [`anthropogenicmetal`](https://w3id.org/isample/vocabulary/material/0.9/anthropogenicmetal)

Child of:
 [`anyanthropogenicmaterial`](#anyanthropogenicmaterial)

Specimen is dominantly composed of metal that has been produced or
used by humans; subclass of anthropogenic material. Samples of
naturally occuring metallic material (e.g. native copper, gold
nuggets) should be considered mineral material. Metallic material is
material that when polished or fractured, shows a lustrous appearance,
and conducts electricity and heat relatively well. Metals are
typically malleable (they can be hammered into thin sheets) or ductile
(can be drawn into wires). The boundaries between metals, nonmetals,
and metalloids fluctuate slightly due to a lack of universally
accepted definitions of the categories involved.
(https://en.wikipedia.org/wiki/Metal). c.f.
http://purl.obolibrary.org/obo/ENVO_01001069

#####  brass

[]{#brass}

Concept: [`brass`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/brass)

Child of:
 [`anthropogenicmetal`](#anthropogenicmetal)

alloy of copper (Cu) and zinc (Zn)

#####  bronze

[]{#bronze}

Concept: [`bronze`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/bronze)

Child of:
 [`anthropogenicmetal`](#anthropogenicmetal)

alloy consisting primarily of copper with subordinate tin;  often
includes other metals

#####  Copper

[]{#copper}

Concept: [`copper`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/copper)

Child of:
 [`anthropogenicmetal`](#anthropogenicmetal)

copper metal, includes copper-rich alloys not identifiable as brass or
bronze.

#####  Gold

[]{#gold}

Concept: [`gold`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/gold)

Child of:
 [`anthropogenicmetal`](#anthropogenicmetal)

a chemical element with atomic number 79; a dense, soft metal that is
easily malleable and ductile. It has a melting point of 1064 degrees
Celsius and a boiling point of 2,807 degrees Celsius. (ChatGPT)

#####  iron

[]{#iron}

Concept: [`iron`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/iron)

Child of:
 [`anthropogenicmetal`](#anthropogenicmetal)

Iron or iron-rich alloy

#####  lead

[]{#lead}

Concept: [`lead`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/lead)

Child of:
 [`anthropogenicmetal`](#anthropogenicmetal)

lead or lead-rich alloy

#####  pewter

[]{#pewter}

Concept: [`pewter`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/pewter)

Child of:
 [`anthropogenicmetal`](#anthropogenicmetal)

alloy consisting of mostly tin,  with antimony,  minor copper or
bismuth, and sometimes silver.

####  Anthropogenic material

[]{#otheranthropogenicmaterial}

Concept: [`otheranthropogenicmaterial`](https://w3id.org/isample/vocabulary/material/0.9/otheranthropogenicmaterial)

Child of:
 [`anyanthropogenicmaterial`](#anyanthropogenicmaterial)

Non-metallic material produced by human activity. Organic products of
agricultural activity are both anthropogenic and organic. Include lab
preparations like XRF pellet and rock powders. Examples: ceramics,
concrete, slag, (anthropogenic) glass, mine tailing, plaster, waste.

#####  Anthropogenic organic material

[]{#anthropogenicorganicmaterial}

Concept: [`anthropogenicorganicmaterial`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/anthropogenicorganicmaterial)

Child of:
 [`organicmaterial`](#organicmaterial)
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

Organic material manufactured by humans

######  Plastic (material)

[]{#plastic}

Concept: [`plastic`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/plastic)

Child of:
 [`anthropogenicorganicmaterial`](#anthropogenicorganicmaterial)

Synthetic or semi-synthetic material that uses organic polymers as a
main ingredient.

See Also:

* [""]()

#####  Ceramic clay

[]{#ceramicclay}

Concept: [`ceramicclay`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/ceramicclay)

Child of:
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

Any of the various hard, brittle, heat-resistant and corrosion-
resistant materials made by shaping and then firing an inorganic,
nonmetallic material, such as clay, at a high temperature.  Common
examples are earthenware, porcelain, and brick.
(https://en.wikipedia.org/wiki/Ceramic)

######  Brick clay

[]{#brickclay}

Concept: [`brickclay`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/brickclay)

Child of:
 [`ceramicclay`](#ceramicclay)

dried or low-fired clay-rich material used to make blocks for
construction

######  bucchero

[]{#bucchero}

Concept: [`bucchero`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/bucchero)

Child of:
 [`ceramicclay`](#ceramicclay)

ceramic with black fabric and glossy, black surface achieved through
reduction firing

######  faience

[]{#faience}

Concept: [`faience`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/faience)

Child of:
 [`ceramicclay`](#ceramicclay)

fine white-glazed ceramic (tin oxide based glaze)

######  Porcelain

[]{#porcelain}

Concept: [`porcelain`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/porcelain)

Child of:
 [`ceramicclay`](#ceramicclay)

Kaolin rich high-fired ceramic; In China, it includes any such ware
that is highly fired enough to produce a ringing sound when struck. In
Europe, it is limited to hard-fired ceramic that is translucent.
(https://vocab.getty.edu/aat/scopeNote/45436)

######  Terracotta

[]{#terracotta}

Concept: [`terracotta`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/terracotta)

Child of:
 [`ceramicclay`](#ceramicclay)

clay-based unglazed or glazed, porous ceramic

######  Terra sigilata

[]{#terrasigilata}

Concept: [`terrasigilata`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/terrasigilata)

Child of:
 [`ceramicclay`](#ceramicclay)

Fine red Ancient Roman pottery with glossy surface slips

#####  Fiber material

[]{#fibermaterial}

Concept: [`fibermaterial`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/fibermaterial)

Child of:
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

material composed of fibers twisted or woved togther. Fibers might be
plant material or Anthropogenic Organic material.

#####  Glass

[]{#glass}

Concept: [`glass`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/glass)

Child of:
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

A non-crystalline, often transparent amorphous solid, most often
formed by rapid cooling (quenching) of the molten silca rich material.
(https://en.wikipedia.org/wiki/Glass)

#####  Paper

[]{#paper}

Concept: [`paper`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/paper)

Child of:
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)


#####  plaster

[]{#plaster}

Concept: [`plaster`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/plaster)

Child of:
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

plaster or mortar

#####  Plaster or Mortar

[]{#plasterormortar}

Concept: [`plasterormortar`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/plasterormortar)

Child of:
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

Plaster is a pasty material that hardens on drying and is used for
coating walls, ceilings, and partitions. Mortar is a similar pasty
material used for cementing bricks or block together or coating walls
in building construction.

#####  Rubber

[]{#rubber}

Concept: [`rubber`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/rubber)

Child of:
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

An elastomer, synthesized from petroleum byproducts or from latex
harvested from the rubber tree (Hevea brasiliensis).

###  Any ice

[]{#anyice}

Concept: [`anyice`](https://w3id.org/isample/vocabulary/material/0.9/anyice)

Child of:
 [`material`](#material)

a solid material that is normally a liquid or gas at Standard
Temperature and Pressre (STP)  that is in a solid state under the
observed temperature and pressure conditions.

####  Frozen water

[]{#waterice}

Concept: [`waterice`](https://w3id.org/isample/vocabulary/material/0.9/waterice)

Child of:
 [`anyice`](#anyice)

Water that is in a solid state.

###  Biogenic non-organic material

[]{#biogenicnonorganicmaterial}

Concept: [`biogenicnonorganicmaterial`](https://w3id.org/isample/vocabulary/material/0.9/biogenicnonorganicmaterial)

Child of:
 [`material`](#material)

Material produced by an organism but not composed of 'very large
molecules of biological origin.' E.g. bone, tooth, shell, coral
skeleton,

####  amber

[]{#amber}

Concept: [`amber`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/amber)

Child of:
 [`biogenicnonorganicmaterial`](#biogenicnonorganicmaterial)


####  bone

[]{#bone}

Concept: [`bone`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/bone)

Child of:
 [`biogenicnonorganicmaterial`](#biogenicnonorganicmaterial)


####  charcoal

[]{#charcoal}

Concept: [`charcoal`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/charcoal)

Child of:
 [`biogenicnonorganicmaterial`](#biogenicnonorganicmaterial)


####  coal

[]{#coal}

Concept: [`coal`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/coal)

Child of:
 [`biogenicnonorganicmaterial`](#biogenicnonorganicmaterial)
 [`rock`](#rock)


####  Shell

[]{#shell}

Concept: [`shell`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/shell)

Child of:
 [`biogenicnonorganicmaterial`](#biogenicnonorganicmaterial)


###  Dispersed media

[]{#dispersedmedia}

Concept: [`dispersedmedia`](https://w3id.org/isample/vocabulary/material/0.9/dispersedmedia)

Child of:
 [`material`](#material)

A material contains discrete elements of one medium that are dispersed
in a continuous fluid medium.  The dispersed component can be a gas, a
liquid or a solid (based on
https://en.wikipedia.org/wiki/Dispersed_media). Does not include
mixtures of granular material like soil, sediment, particulate, or
solids that would be considered a rock. E.g. aerosol ENVO_00010505,
foam ENVO_00005738, emulsion ENVO_00010506, colloidal suspension
ENVO_01001560, scum(?)ENVO:00003930, clathrate?

###  Natural Solid Material

[]{#earthmaterial}

Concept: [`earthmaterial`](https://w3id.org/isample/vocabulary/material/0.9/earthmaterial)

Child of:
 [`material`](#material)

Undifferentiated soil, sediment, rock, or natural particulates.
Typically (nessarily?) a granular aggregate that might include any of
the previous constiturents. Use for Earth Material aggregates of
uncertain origin

####  Mineral

[]{#mineral}

Concept: [`mineral`](https://w3id.org/isample/vocabulary/material/0.9/mineral)

Child of:
 [`earthmaterial`](#earthmaterial)

Material consists of a single mineral or mineraloid phase. .  'A
mineral is an element or chemical compound that is normally
crystalline and that has been formed as a result of geological
processes.' (Nickel, Ernest H. (1995), The definition of a mineral,
The Canadian Mineralogist. 33 (3): 689–90). Include mineraloids. ... A
material primarily composed of some substance that is naturally
occurring, solid and stable at room temperature, representable by a
chemical formula, usually abiogenic, and that has an ordered atomic
structure. (http://purl.obolibrary.org/obo/ENVO_01000256). Comment:
the identity of a mineral species is defined by a crystal structure
and a chemical composition that might include various specific
elemental substitutions in that structure. Mineraloid: A naturally
occurring mineral-like substance that does not demonstrate
crystallinity. Mineraloids possess chemical compositions that vary
beyond the generally accepted ranges for specific minerals. Examples:
obsidian, Opal. (https://en.wikipedia.org/wiki/Mineraloid)

#####  Hematite

[]{#hematite}

Concept: [`hematite`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/hematite)

Child of:
 [`mineral`](#mineral)


#####  kaolin

[]{#kaolin}

Concept: [`kaolin`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/kaolin)

Child of:
 [`mineral`](#mineral)


#####  mica

[]{#mica}

Concept: [`mica`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/mica)

Child of:
 [`mineral`](#mineral)


#####  quartz

[]{#quartz}

Concept: [`quartz`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/quartz)

Child of:
 [`mineral`](#mineral)


#####  Mineral-Borate

[]{#boratemineral}

Concept: [`boratemineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/boratemineral)

Child of:
 [`mineral`](#mineral)

Minerals which contain a borate anion group.

#####  Mineral-Carbonate or Nitrate

[]{#carbonatenitratemineral}

Concept: [`carbonatenitratemineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/carbonatenitratemineral)

Child of:
 [`mineral`](#mineral)

Carbonate minerals are those minerals containing the carbonate ion

#####  Mineral-Halide

[]{#halidemineral}

Concept: [`halidemineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/halidemineral)

Child of:
 [`mineral`](#mineral)

Minerals with a dominant halide anion.

#####  Mineral-Native Element

[]{#nativeelementmineral}

Concept: [`nativeelementmineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/nativeelementmineral)

Child of:
 [`mineral`](#mineral)

Elements that occur in nature in uncombined form with a distinct
mineral structure. Includes metals and intermetallic alloys;
metalloids and nonmetals; carbides, silicides, nitrides, phosphides

#####  Mineral-Organic Compound

[]{#organicmineral}

Concept: [`organicmineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/organicmineral)

Child of:
 [`mineral`](#mineral)

Salts of organic acids, hydrocarbons, and miscellaneous organic
minerals formed as a result of geological processes. Includes
hydrocarbons, formates, acetates, oxalates, benzine salts, cyanates.
Chemical compounds in which one or more atoms of carbon are covalently
linked to atoms of other elements, most commonly hydrogen, oxygen, or
nitrogen (https://www.britannica.com/science/organic-compound).

#####  Mineral-Oxide

[]{#oxidemineral}

Concept: [`oxidemineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/oxidemineral)

Child of:
 [`mineral`](#mineral)

Includes class oxides, hydroxides, and arsenties. Oxides are minerals
in which the oxide anion is bonded to one or more metal alloys. The
hydroxide-bearing minerals are typically included in the oxide class.
Arsenite minerals are very rare oxygen-bearing arsenic minerals.

#####  Mineral-Phosphate, Arsenate, or Vanadate

[]{#phosphatearsenatevanadatemineral}

Concept: [`phosphatearsenatevanadatemineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/phosphatearsenatevanadatemineral)

Child of:
 [`mineral`](#mineral)

Phosphate minerals contain the phosphate anion along sometimes with
arsenate and vanadate substitutions, and chloride, fluoride, and
hydroxide anions that also fit into the crystal structure. Arsenate
minerals usually refer to the naturally occurring orthoarsenates.

#####  Mineral-Silicate or Germanate

[]{#silicategermanatemineral}

Concept: [`silicategermanatemineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/silicategermanatemineral)

Child of:
 [`mineral`](#mineral)

Rock-forming minerals made up of silicate groups

#####  Mineral-Sulfate, Selenate, or Tellurate

[]{#sulfateselenatetelluratemineral}

Concept: [`sulfateselenatetelluratemineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/sulfateselenatetelluratemineral)

Child of:
 [`mineral`](#mineral)

class of minerals that include the sulfate ion within their structure.

#####  Mineral-Sulfide or Sulfosalt

[]{#sulfidesulfosaltmineral}

Concept: [`sulfidesulfosaltmineral`](https://w3id.org/isample/vocabulary/mingroup/0.9/sulfidesulfosaltmineral)

Child of:
 [`mineral`](#mineral)

Sulfide minerals are a class of minerals containing sulfide or
disulfide as the major anion. Sulfosalt minerals are those complex
sulfide minerals with the general formula: AmBnSp; where A represents
a metal such as copper, lead, silver, iron, and rarely mercury, zinc,
vanadium; B usually represents semi-metal such as arsenic, antimony,
bismuth, and rarely germanium, or metals like tin and rarely vanadium;
and S is sulfur or rarely selenium or/and tellurium (m, n, and p are
integer formula subscripts). Includes sulfides, selenides, tellurides;
arsenides, antimonides, bismuthides; sulfarsenites, sulfantimonites,
sulfbismuthites

####  Mixed soil sediment or rock

[]{#mixedsoilsedimentrock}

Concept: [`mixedsoilsedimentrock`](https://w3id.org/isample/vocabulary/material/0.9/mixedsoilsedimentrock)

Child of:
 [`earthmaterial`](#earthmaterial)

Material is mixed aggregation of fragments of undifferentiated soil,
sediment or  rock origin. e.g. cuttings from some boreholes (rock
fragments and caved soil or sediment), sea floor dredge haul (mixed
sediment and rock)

####  Particulate

[]{#particulate}

Concept: [`particulate`](https://w3id.org/isample/vocabulary/material/0.9/particulate)

Child of:
 [`earthmaterial`](#earthmaterial)

Material consists of microscopic particulate material derived by
precipitation, filtering, or settling from suspension in a fluid, e.g.
filtrate from water, deposition from atmosphere, astro material
particles. Might include mineral, organic, or biological material.
ENVO definition (ENVO_01000060) has "composed of microscopic portions
of solid or liquid material suspended in another environmental
material.", refine here to define as the solid particles, distinct
from a material in which they are suspended. A material that includes
solid or liquid particles suspended in another material would be a
dispersed_media in this scheme, not defined in ENVO. Human
manufactured particulates (e.g. rock powder) should be categorized as
'anthropogenic material' as well as 'Particulate'

#####  Cinder

[]{#cinder}

Concept: [`cinder`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/cinder)

Child of:
 [`rock`](#rock)
 [`particulate`](#particulate)

The incombustible residue of something burnt.@en

####  Rock or sediment

[]{#rockorsediment}

Concept: [`rockorsediment`](https://w3id.org/isample/vocabulary/material/0.9/rockorsediment)

Child of:
 [`earthmaterial`](#earthmaterial)

Material is rock or sediment.  E.g. for samples from subsurface cores
that are not well described, from drill holes that likely penetrate
sediment near the surface an might be sampling rock at greater depth.

#####  Rock

[]{#rock}

Concept: [`rock`](https://w3id.org/isample/vocabulary/material/0.9/rock)

Child of:
 [`rockorsediment`](#rockorsediment)

Consolidated aggregate of particles (grains) of rock, mineral
(including native elements), mineraloid, or solid organic material.
Includes mineral aggregates such as granite, shale, marble; natural
glass such as obsidian; organic material formed by geologic processes
such a coal;  extraterrestrial material in meteorites; and  crushed
rock fragments like drill cuttings from rock.  (based on
http://resource.geosciml.org/classifier/cgi/lithology/rock, same as
http://purl.obolibrary.org/obo/ENVO_00001995)

See Also:

* [<http://purl.obolibrary.org/obo/ENVO_00001995>](http://purl.obolibrary.org/obo/ENVO_00001995)
* [<http://resource.geosciml.org/classifier/cgi/lithology/rock>](http://resource.geosciml.org/classifier/cgi/lithology/rock)

######  Basalt

[]{#basalt}

Concept: [`basalt`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/basalt)

Child of:
 [`rock`](#rock)


######  Chert

[]{#chert}

Concept: [`chert`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/chert)

Child of:
 [`rock`](#rock)


#######  flint

[]{#flint}

Concept: [`flint`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/flint)

Child of:
 [`chert`](#chert)


######  Cinder

[]{#cinder}

Concept: [`cinder`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/cinder)

Child of:
 [`rock`](#rock)
 [`particulate`](#particulate)

The incombustible residue of something burnt.@en

######  coal

[]{#coal}

Concept: [`coal`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/coal)

Child of:
 [`biogenicnonorganicmaterial`](#biogenicnonorganicmaterial)
 [`rock`](#rock)


######  dolomite

[]{#dolomite}

Concept: [`dolomite`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/dolomite)

Child of:
 [`rock`](#rock)


######  gabbro

[]{#gabbro}

Concept: [`gabbro`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/gabbro)

Child of:
 [`rock`](#rock)


######  greywacke

[]{#greywacke}

Concept: [`greywacke`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/greywacke)

Child of:
 [`rock`](#rock)


######  limestone

[]{#limestone}

Concept: [`limestone`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/limestone)

Child of:
 [`rock`](#rock)


######  marble

[]{#marble}

Concept: [`marble`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/marble)

Child of:
 [`rock`](#rock)


######  obsidian

[]{#obsidian}

Concept: [`obsidian`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/obsidian)

Child of:
 [`rock`](#rock)


######  pumice

[]{#pumice}

Concept: [`pumice`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/pumice)

Child of:
 [`rock`](#rock)


######  Slate

[]{#slate}

Concept: [`slate`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/slate)

Child of:
 [`rock`](#rock)


######  Travertine

[]{#travertine}

Concept: [`travertine`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/travertine)

Child of:
 [`rock`](#rock)


######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Aphanite`
[]{#aphanite}

Concept: [`Aphanite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Aphanite)

Child of:
 [`rock`](#rock)

Rock that is too fine grained to categorize in more detail.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Breccia`
[]{#breccia}

Concept: [`Breccia`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Breccia)

Child of:
 [`rock`](#rock)

Coarse-grained material composed of angular broken rock fragments; the
fragments typically have sharp edges and unworn corners. The fragments
may be held together by a mineral cement or in a fine-grained matrix,
and consolidated or nonconsolidated. Clasts may be of any composition
or origin. In sedimentary environments, breccia is used for material
that consists entirely of angular fragments, mostly derived from a
single source rock body, as in a rock avalanche deposit, and matrix is
interpreted to be the product of comminution of clasts during
transport. Diamictite or diamicton is used when the material reflects
mixing of rock from a variety of sources, some sub angular or
subrounded clasts may be present, and matrix is pre-existing fine
grained material that is not a direct product of the
brecciation/deposition process.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Fault_Related_Material`
[]{#fault_related_material}

Concept: [`Fault_Related_Material`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Fault_Related_Material)

Child of:
 [`rock`](#rock)

Material formed as a result brittle faulting, composed of greater than
10 percent matrix; matrix is fine-grained material caused by tectonic
grainsize reduction. Includes cohesive (cataclasite series, mylonitic
rocks) and non-cohesive (breccia-gouge series) material.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Cataclasite_Series`
[]{#cataclasite_series}

Concept: [`Cataclasite_Series`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Cataclasite_Series)

Child of:
 [`Fault_Related_Material`](#Fault_Related_Material)

Fault-related rock that maintained primary cohesion during
deformation, with matrix comprising greater than 10 percent of rock
mass; matrix is fine-grained material formed through grain size
reduction by fracture as opposed to crystal plastic process that
operate in mylonitic rock. Includes cataclasite, protocataclasite and
ultracataclasite.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Mylonitic_Rock`
[]{#mylonitic_rock}

Concept: [`Mylonitic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Mylonitic_Rock)

Child of:
 [`Fault_Related_Material`](#Fault_Related_Material)

Metamorphic rock characterised by a foliation resulting from tectonic
grain size reduction, in which more than 10 percent of the rock volume
has undergone grain size reduction. Includes protomylonite, mylonite,
ultramylonite, and blastomylonite.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/breccia_gouge_series`
[]{#breccia_gouge_series}

Concept: [`breccia_gouge_series`](https://w3id.org/isample/vocabulary/rocksediment/0.9/breccia_gouge_series)

Child of:
 [`Fault_Related_Material`](#Fault_Related_Material)

Fault-related material with features such as void spaces (filled or
unfilled), or unconsolidated matrix material between fragments,
indicating loss of cohesion during deformation. Includes fault-related
breccia and gouge.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Fragmental_Igneous_Rock`
[]{#fragmental_igneous_rock}

Concept: [`Fragmental_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Fragmental_Igneous_Rock)

Child of:
 [`rock`](#rock)
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock in which greater than 75 percent of the rock consists of
fragments produced as a result of igneous rock-forming process.
Includes pyroclastic rocks, autobreccia associated with lava flows and
intrusive breccias. Excludes deposits reworked by epiclastic processes
(see Tuffite)

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroclastic_Rock`
[]{#pyroclastic_rock}

Concept: [`Pyroclastic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroclastic_Rock)

Child of:
 [`Fragmental_Igneous_Rock`](#Fragmental_Igneous_Rock)

Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Igneous_Rock`
[]{#igneous_rock}

Concept: [`Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Igneous_Rock)

Child of:
 [`rock`](#rock)

rock formed as a result of igneous processes, for example intrusion
and cooling of magma in the crust, or volcanic eruption.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Acidic_Igneous_Rock`
[]{#acidic_igneous_rock}

Concept: [`Acidic_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Acidic_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock with more than 63 percent SiO2.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Dacite`
[]{#dacite}

Concept: [`Dacite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Dacite)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine grained or porphyritic crystalline rock that contains less than
90 percent mafic minerals, between 20 and 60 percent quartz in the
QAPF fraction, and has a plagioclase to total feldspar ratio greater
than 0.65. Includes rocks defined modally in QAPF fields 4 and 5 or
chemically in TAS Field O3. Typically composed of quartz and sodic
plagioclase with minor amounts of biotite and/or hornblende and/or
pyroxene; fine-grained equivalent of granodiorite and tonalite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Granitoid`
[]{#granitoid}

Concept: [`Granitoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Granitoid)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock consisting of quartz, alkali
feldspar and/or plagioclase. Includes rocks defined modally in QAPF
fields 2, 3, 4 and 5 as alkali feldspar granite, granite, granodiorite
or tonalite.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Alkali_Feldspar_Granite`
[]{#alkali_feldspar_granite}

Concept: [`Alkali_Feldspar_Granite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Alkali_Feldspar_Granite)

Child of:
 [`Granitoid`](#Granitoid)

Granitic rock that has a plagioclase to total feldspar ratio less than
0.1. QAPF field 2.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Granite`
[]{#granite}

Concept: [`Granite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Granite)

Child of:
 [`Granitoid`](#Granitoid)

Phaneritic crystalline rock consisting of quartz, alkali feldspar and
plagioclase (typically sodic) in variable amounts, usually with
biotite and/or hornblende. Includes rocks defined modally in QAPF
Field 3.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Granodiorite`
[]{#granodiorite}

Concept: [`Granodiorite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Granodiorite)

Child of:
 [`Granitoid`](#Granitoid)

Phaneritic crystalline rock consisting essentially of quartz, sodic
plagioclase and lesser amounts of alkali feldspar with minor
hornblende and biotite. Includes rocks defined modally in QAPF field
4.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Tonalite`
[]{#tonalite}

Concept: [`Tonalite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Tonalite)

Child of:
 [`Granitoid`](#Granitoid)

Granitoid consisting of quartz and intermediate plagioclase, usually
with biotite and amphibole. Includes rocks defined modally in QAPF
field 5; ratio of plagioclase to total feldspar is greater than 0.9.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Quartz_Rich_Igneous_Rock`
[]{#quartz_rich_igneous_rock}

Concept: [`Quartz_Rich_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Quartz_Rich_Igneous_Rock)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Occurrence of igneous rocks meeting this criteria seems to be
vanishingly rare, thus subdividing the category does not seem
warranted for the purposes of This vocabulary. Future usage of the
vocabulary may motivate including quatzolite and quartz-rich granitoid
in future revisions
Phaneritic crystalline igneous rock that contains less than 90 percent
mafic minerals and contains greater than 60 percent quartz in the QAPF
fraction.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Rhyolitoid`
[]{#rhyolitoid}

Concept: [`Rhyolitoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Rhyolitoid)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Note that technical definition, based on modal mineralogy plotted in a
QAPF triangle may be applied qualitatively, based on phenocryst
mineralogy when ground mass mineralogy can not be determined
optically, or based on CIPW norm. Although TAS categories are defined
based on chemical analyses, the correspondence with the QAPF defined
categories is generally close enough that QAPF categories are commonly
used interchangeably with TAS categories. It is important to note the
basis for assignment of fine-grained igneous rocks to a specifice
lithology category.
fine_grained_igneous_rock consisting of quartz and alkali feldspar,
with minor plagioclase and biotite, in a microcrystalline,
cryptocrystalline or glassy groundmass. Flow texture is common.
Includes rocks defined modally in QAPF fields 2 and 3 or chemically in
TAS Field R as rhyolite. QAPF normative definition is based on modal
mineralogy thus: less than 90 percent mafic minerals, between 20 and
60 percent quartz in the QAPF fraction, and ratio of plagioclse to
total feldspar is less than 0.65.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Basic_Igneous_Rock`
[]{#basic_igneous_rock}

Concept: [`Basic_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Basic_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock with between 45 and 52 percent SiO2.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Basalt`
[]{#basalt}

Concept: [`Basalt`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Basalt)

Child of:
 [`Basic_Igneous_Rock`](#Basic_Igneous_Rock)
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine-grained or porphyritic igneous rock with less than 20 percent
quartz, and less than 10 percent feldspathoid minerals, in which the
ratio of plagioclase to total feldspar is greater 0.65. Typically
composed of calcic plagioclase and clinopyroxene; phenocrysts
typically include one or more of calcic plagioclase, clinopyroxene,
orthopyroxene, and olivine. Includes rocks defined modally in QAPF
fields 9 and 10 or chemically in TAS field B as basalt. Basalt and
andesite are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Gabbroic_Rock`
[]{#gabbroic_rock}

Concept: [`Gabbroic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Gabbroic_Rock)

Child of:
 [`Basic_Igneous_Rock`](#Basic_Igneous_Rock)
 [`Gabbroid`](#Gabbroid)

Gabbroid that has a plagioclase to total feldspar ratio greater than
0.9 in the QAPF fraction. Includes QAPF fields 10*, 10, and 10'. This
category includes the various categories defined in LeMaitre et al.
(2002) based on the mafic mineralogy, but apparently not subdivided
based on the quartz/feldspathoid content.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Doleritic_Rock`
[]{#doleritic_rock}

Concept: [`Doleritic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Doleritic_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Dark colored gabbroic (basaltic) or dioritic (andesitic) rock
intermediate in grain size between basalt and gabbro and composed of
plagioclase, pyroxene and opaque minerals; often with ophitic texture.
Typically occurs as hypabyssal intrusions. Includes dolerite,
microdiorite, diabase and microgabbro.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Exotic_Composition_Igneous_Rock`
[]{#exotic_composition_igneous_rock}

Concept: [`Exotic_Composition_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Exotic_Composition_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Rock with 'exotic' mineralogical, textural or field setting
characteristics; typically dark colored, with abundant phenocrysts.
Criteria include: presence of greater than 10 percent melilite or
leucite, or presence of kalsilite, or greater than 50 percent
carbonate minerals. Includes Carbonatite, Melilitic rock, Kalsilitic
rocks, Kimberlite, Lamproite, Leucitic rock and Lamprophyres.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Fine_Grained_Igneous_Rock`
[]{#fine_grained_igneous_rock}

Concept: [`Fine_Grained_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Fine_Grained_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock in which the framework of the rock consists of crystals
that are too small to determine mineralogy with the unaided eye;
framework may include up to 50 percent glass. A significant percentage
of the rock by volume may be phenocrysts. Includes rocks that are
generally called volcanic rocks.
Need to make decision as to whether devitrified glass should be
considered glass or microcrystalline framework for purposes of
categorization

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Andesite`
[]{#andesite}

Concept: [`Andesite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Andesite)

Child of:
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)
 [`Intermediate_Composition_Igneous_Rock`](#Intermediate_Composition_Igneous_Rock)

Fine-grained igneous rock with less than 20 percent quartz and less
than 10 percent feldspathoid minerals in the QAPF fraction, in which
the ratio of plagioclase to total feldspar is greater 0.65. Includes
rocks defined modally in QAPF fields 9 and 10 or chemically in TAS
field O2 as andesite. Basalt and andesite, which share the same QAPF
fields, are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight. Typically consists of plagioclase
(frequently zoned from labradorite to oligoclase), pyroxene,
hornblende and/or biotite. Fine grained equivalent of dioritic rock.
Note the mela-andesite and leuco-basalt categories are not recommended
in this system. If chemical analytical data are available to constrain
the silica content, the basalt or andesite category should be used.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Basalt`
[]{#basalt}

Concept: [`Basalt`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Basalt)

Child of:
 [`Basic_Igneous_Rock`](#Basic_Igneous_Rock)
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine-grained or porphyritic igneous rock with less than 20 percent
quartz, and less than 10 percent feldspathoid minerals, in which the
ratio of plagioclase to total feldspar is greater 0.65. Typically
composed of calcic plagioclase and clinopyroxene; phenocrysts
typically include one or more of calcic plagioclase, clinopyroxene,
orthopyroxene, and olivine. Includes rocks defined modally in QAPF
fields 9 and 10 or chemically in TAS field B as basalt. Basalt and
andesite are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Dacite`
[]{#dacite}

Concept: [`Dacite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Dacite)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine grained or porphyritic crystalline rock that contains less than
90 percent mafic minerals, between 20 and 60 percent quartz in the
QAPF fraction, and has a plagioclase to total feldspar ratio greater
than 0.65. Includes rocks defined modally in QAPF fields 4 and 5 or
chemically in TAS Field O3. Typically composed of quartz and sodic
plagioclase with minor amounts of biotite and/or hornblende and/or
pyroxene; fine-grained equivalent of granodiorite and tonalite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Foiditoid`
[]{#foiditoid}

Concept: [`Foiditoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Foiditoid)

Child of:
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine grained crystalline rock containing less than 90 percent mafic
minerals and more than 60 percent feldspathoid minerals in the QAPF
fraction. Includes rocks defined modally in QAPF field 15 or
chemically in TAS field F.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/High_Magnesium_Fine_Grained_Igneous_Rock`
[]{#high_magnesium_fine_grained_igneous_rock}

Concept: [`High_Magnesium_Fine_Grained_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/High_Magnesium_Fine_Grained_Igneous_Rock)

Child of:
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

fine-grained igneous rock that contains unusually high concentration
of MgO. For rocks that contain greater than 52 percent silica, MgO
must be greater than 8 percent. For rocks containing less than 52
percent silica, MgO must be greater than 12 percent.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Phonolitoid`
[]{#phonolitoid}

Concept: [`Phonolitoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Phonolitoid)

Child of:
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine grained igneous rock than contains less than 90 percent mafic
minerals, between 10 and 60 percent feldspathoid mineral in the QAPF
fraction and has a plagioclase to total feldspar ratio less than 0.5.
Includes rocks defined modally in QAPF fields 11 and 12, and TAS field
Ph.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Rhyolitoid`
[]{#rhyolitoid}

Concept: [`Rhyolitoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Rhyolitoid)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Note that technical definition, based on modal mineralogy plotted in a
QAPF triangle may be applied qualitatively, based on phenocryst
mineralogy when ground mass mineralogy can not be determined
optically, or based on CIPW norm. Although TAS categories are defined
based on chemical analyses, the correspondence with the QAPF defined
categories is generally close enough that QAPF categories are commonly
used interchangeably with TAS categories. It is important to note the
basis for assignment of fine-grained igneous rocks to a specifice
lithology category.
fine_grained_igneous_rock consisting of quartz and alkali feldspar,
with minor plagioclase and biotite, in a microcrystalline,
cryptocrystalline or glassy groundmass. Flow texture is common.
Includes rocks defined modally in QAPF fields 2 and 3 or chemically in
TAS Field R as rhyolite. QAPF normative definition is based on modal
mineralogy thus: less than 90 percent mafic minerals, between 20 and
60 percent quartz in the QAPF fraction, and ratio of plagioclse to
total feldspar is less than 0.65.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Tephritoid`
[]{#tephritoid}

Concept: [`Tephritoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Tephritoid)

Child of:
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine grained igneous rock than contains less than 90 percent mafic
minerals, between 10 and 60 percent feldspathoid mineral in the QAPF
fraction and has a plagioclase to total feldspar ratio greater than
0.5. Includes rocks classified in QAPF field 13 and 14 or chemically
in TAS field U1 as basanite or tephrite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Trachytoid`
[]{#trachytoid}

Concept: [`Trachytoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Trachytoid)

Child of:
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)

Fine grained igneous rock than contains less than 90 percent mafic
minerals, less than 10 percent feldspathoid mineral and less than 20
percent quartz in the QAPF fraction and has a plagioclase to total
feldspar ratio less than 0.65. Mafic minerals typically include
amphibole or mica; typically porphyritic. Includes rocks defined
modally in QAPF fields 6, 7 and 8 (with subdivisions) or chemically in
TAS Field T as trachyte or latite.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Fragmental_Igneous_Rock`
[]{#fragmental_igneous_rock}

Concept: [`Fragmental_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Fragmental_Igneous_Rock)

Child of:
 [`rock`](#rock)
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock in which greater than 75 percent of the rock consists of
fragments produced as a result of igneous rock-forming process.
Includes pyroclastic rocks, autobreccia associated with lava flows and
intrusive breccias. Excludes deposits reworked by epiclastic processes
(see Tuffite)

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroclastic_Rock`
[]{#pyroclastic_rock}

Concept: [`Pyroclastic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroclastic_Rock)

Child of:
 [`Fragmental_Igneous_Rock`](#Fragmental_Igneous_Rock)

Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Glass_Rich_Igneous_Rock`
[]{#glass_rich_igneous_rock}

Concept: [`Glass_Rich_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Glass_Rich_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock that contains greater than 50 percent massive glass.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Hypabyssal_Intrusive_Rock`
[]{#hypabyssal_intrusive_rock}

Concept: [`Hypabyssal_Intrusive_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Hypabyssal_Intrusive_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rocks formed by crystallisation close to the Earth's surface,
characterized by more rapid cooling than plutonic setting to produce
generally fine-grained intrusive igneous rock, commonly associated
with co-magmatic volcanic rocks.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Intermediate_Composition_Igneous_Rock`
[]{#intermediate_composition_igneous_rock}

Concept: [`Intermediate_Composition_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Intermediate_Composition_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock with between 52 and 63 percent SiO2.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Andesite`
[]{#andesite}

Concept: [`Andesite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Andesite)

Child of:
 [`Fine_Grained_Igneous_Rock`](#Fine_Grained_Igneous_Rock)
 [`Intermediate_Composition_Igneous_Rock`](#Intermediate_Composition_Igneous_Rock)

Fine-grained igneous rock with less than 20 percent quartz and less
than 10 percent feldspathoid minerals in the QAPF fraction, in which
the ratio of plagioclase to total feldspar is greater 0.65. Includes
rocks defined modally in QAPF fields 9 and 10 or chemically in TAS
field O2 as andesite. Basalt and andesite, which share the same QAPF
fields, are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight. Typically consists of plagioclase
(frequently zoned from labradorite to oligoclase), pyroxene,
hornblende and/or biotite. Fine grained equivalent of dioritic rock.
Note the mela-andesite and leuco-basalt categories are not recommended
in this system. If chemical analytical data are available to constrain
the silica content, the basalt or andesite category should be used.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Dioritoid`
[]{#dioritoid}

Concept: [`Dioritoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Dioritoid)

Child of:
 [`Intermediate_Composition_Igneous_Rock`](#Intermediate_Composition_Igneous_Rock)
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock with M less than 90, consisting of
intermediate plagioclase, commonly with hornblende and often with
biotite or augite. Plagioclase to total feldspar ratio is greater that
0.65, and anorthite content of plagioclase is less than 50 percent.
Less than 10 percent feldspathoid mineral and less than 20 percent
quartz in the QAPF fraction. Includes rocks defined modally in QAPF
fields 9 and 10 (and their subdivisions).

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Phaneritic_Igneous_Rock`
[]{#phaneritic_igneous_rock}

Concept: [`Phaneritic_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Phaneritic_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock in which the framework of the rock consists of individual
crystals that can be discerned with the unaided eye. Bounding grain
size is on the order of 32 to 100 microns. Igneous rocks with 'exotic'
composition are excluded from this concept.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Anorthositic_Rock`
[]{#anorthositic_rock}

Concept: [`Anorthositic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Anorthositic_Rock)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Anorthositic rock term invented to label the combined QAPF fields 10,
10*, and 10', in order to construct hierarchy in this vocabulary.
Leucocratic phaneritic crystalline igneous rock consisting essentially
of plagioclase, often with small amounts of pyroxene. By definition,
colour index M is less than 10, and plagiclase to total feldspar ratio
is greater than 0.9. Less than 20 percent quartz and less than 10
percent feldspathoid in the QAPF fraction. QAPF field 10, 10*, and
10'.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Aplite`
[]{#aplite}

Concept: [`Aplite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Aplite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Light coloured crystalline rock, characterized by a fine grained
allotriomorphic-granular (aplitic, saccharoidal or xenomorphic)
texture; typically granitic composition, consisting of quartz, alkali
feldspar and sodic plagioclase.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Dioritoid`
[]{#dioritoid}

Concept: [`Dioritoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Dioritoid)

Child of:
 [`Intermediate_Composition_Igneous_Rock`](#Intermediate_Composition_Igneous_Rock)
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock with M less than 90, consisting of
intermediate plagioclase, commonly with hornblende and often with
biotite or augite. Plagioclase to total feldspar ratio is greater that
0.65, and anorthite content of plagioclase is less than 50 percent.
Less than 10 percent feldspathoid mineral and less than 20 percent
quartz in the QAPF fraction. Includes rocks defined modally in QAPF
fields 9 and 10 (and their subdivisions).

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Foid_Dioritoid`
[]{#foid_dioritoid}

Concept: [`Foid_Dioritoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Foid_Dioritoid)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock in which M is less than 90, the
plagioclase to total feldspar ratio is greater than 0.5, feldspathoid
minerals form 10-60 percent of the QAPF fraction, plagioclase has
anorthite content less than 50 percent. These rocks typically contain
large amounts of mafic minerals. Includes rocks defined modally in
QAPF fields 13 and 14.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Foid_Gabbroid`
[]{#foid_gabbroid}

Concept: [`Foid_Gabbroid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Foid_Gabbroid)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock in which M is less than 90, the
plagioclase to total feldspar ratio is greater than 0.5, feldspathoids
form 10-60 percent of the QAPF fraction, and plagioclase has anorthite
content greater than 50 percent. These rocks typically contain large
amounts of mafic minerals. Includes rocks defined modally in QAPF
fields 13 and 14.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Foid_Syenitoid`
[]{#foid_syenitoid}

Concept: [`Foid_Syenitoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Foid_Syenitoid)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock with M less than 90, contains
between 10 and 60 percent feldspathoid mineral in the QAPF fraction,
and has a plagioclase to total feldspar ratio less than 0.5. Includes
QAPF fields 11 and 12.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Foidolite`
[]{#foidolite}

Concept: [`Foidolite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Foidolite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline rock containing more than 60 percent
feldspathoid minerals in the QAPF fraction. Includes rocks defined
modally in QAPF field 15

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Gabbroid`
[]{#gabbroid}

Concept: [`Gabbroid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Gabbroid)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock that contains less than 90 percent
mafic minerals, and up to 20 percent quartz or up to 10 percent
feldspathoid in the QAPF fraction. The ratio of plagioclase to total
feldspar is greater than 0.65, and anorthite content of the
plagioclase is greater than 50 percent. Includes rocks defined modally
in QAPF fields 9 and 10 and their subdivisions.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Gabbroic_Rock`
[]{#gabbroic_rock}

Concept: [`Gabbroic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Gabbroic_Rock)

Child of:
 [`Basic_Igneous_Rock`](#Basic_Igneous_Rock)
 [`Gabbroid`](#Gabbroid)

Gabbroid that has a plagioclase to total feldspar ratio greater than
0.9 in the QAPF fraction. Includes QAPF fields 10*, 10, and 10'. This
category includes the various categories defined in LeMaitre et al.
(2002) based on the mafic mineralogy, but apparently not subdivided
based on the quartz/feldspathoid content.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Monzogabbroic_Rock`
[]{#monzogabbroic_rock}

Concept: [`Monzogabbroic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Monzogabbroic_Rock)

Child of:
 [`Gabbroid`](#Gabbroid)

Gabbroid with a plagioclase to total feldspar ratio between 0.65 and
0.9. QAPF field 9, 9 prime and 9 asterisk

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Granitoid`
[]{#granitoid}

Concept: [`Granitoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Granitoid)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock consisting of quartz, alkali
feldspar and/or plagioclase. Includes rocks defined modally in QAPF
fields 2, 3, 4 and 5 as alkali feldspar granite, granite, granodiorite
or tonalite.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Alkali_Feldspar_Granite`
[]{#alkali_feldspar_granite}

Concept: [`Alkali_Feldspar_Granite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Alkali_Feldspar_Granite)

Child of:
 [`Granitoid`](#Granitoid)

Granitic rock that has a plagioclase to total feldspar ratio less than
0.1. QAPF field 2.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Granite`
[]{#granite}

Concept: [`Granite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Granite)

Child of:
 [`Granitoid`](#Granitoid)

Phaneritic crystalline rock consisting of quartz, alkali feldspar and
plagioclase (typically sodic) in variable amounts, usually with
biotite and/or hornblende. Includes rocks defined modally in QAPF
Field 3.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Granodiorite`
[]{#granodiorite}

Concept: [`Granodiorite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Granodiorite)

Child of:
 [`Granitoid`](#Granitoid)

Phaneritic crystalline rock consisting essentially of quartz, sodic
plagioclase and lesser amounts of alkali feldspar with minor
hornblende and biotite. Includes rocks defined modally in QAPF field
4.

#########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Tonalite`
[]{#tonalite}

Concept: [`Tonalite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Tonalite)

Child of:
 [`Granitoid`](#Granitoid)

Granitoid consisting of quartz and intermediate plagioclase, usually
with biotite and amphibole. Includes rocks defined modally in QAPF
field 5; ratio of plagioclase to total feldspar is greater than 0.9.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Hornblendite`
[]{#hornblendite}

Concept: [`Hornblendite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Hornblendite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)
 [`Ultramafic_Igneous_Rock`](#Ultramafic_Igneous_Rock)

Ultramafic rock that consists of greater than 40 percent hornblende
plus pyroxene and has a hornblende to pyroxene ratio greater than 1.
Includes olivine hornblendite, olivine-pyroxene hornblendite, pyroxene
hornblendite, and hornblendite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Pegmatite`
[]{#pegmatite}

Concept: [`Pegmatite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Pegmatite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Exceptionally coarse grained crystalline rock with interlocking
crystals; most grains are 1cm or more diameter; composition is
generally that of granite, but the term may refer to the coarse
grained facies of any type of igneous rock;usually found as irregular
dikes, lenses, or veins associated with plutons or batholiths.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Peridotite`
[]{#peridotite}

Concept: [`Peridotite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Peridotite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)
 [`Ultramafic_Igneous_Rock`](#Ultramafic_Igneous_Rock)

Ultramafic rock consisting of more than 40 percent (by volume) olivine
with pyroxene and/or amphibole and little or no feldspar. commonly
altered to serpentinite. Includes rocks defined modally in the
ultramafic rock classification as dunite, harzburgite, lherzolite,
wehrlite, olivinite, pyroxene peridotite, pyroxene hornblende
peridotite or hornblende peridotite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroxenite`
[]{#pyroxenite}

Concept: [`Pyroxenite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroxenite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)
 [`Ultramafic_Igneous_Rock`](#Ultramafic_Igneous_Rock)

Ultramafic phaneritic igneous rock composed almost entirely of one or
more pyroxenes and occasionally biotite, hornblende and olivine.
Includes rocks defined modally in the ultramafic rock classification
as olivine pyroxenite, olivine-hornblende pyroxenite, pyroxenite,
orthopyroxenite, clinopyroxenite and websterite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Quartz_Rich_Igneous_Rock`
[]{#quartz_rich_igneous_rock}

Concept: [`Quartz_Rich_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Quartz_Rich_Igneous_Rock)

Child of:
 [`Acidic_Igneous_Rock`](#Acidic_Igneous_Rock)
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Occurrence of igneous rocks meeting this criteria seems to be
vanishingly rare, thus subdividing the category does not seem
warranted for the purposes of This vocabulary. Future usage of the
vocabulary may motivate including quatzolite and quartz-rich granitoid
in future revisions
Phaneritic crystalline igneous rock that contains less than 90 percent
mafic minerals and contains greater than 60 percent quartz in the QAPF
fraction.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Syenitoid`
[]{#syenitoid}

Concept: [`Syenitoid`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Syenitoid)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)

Phaneritic crystalline igneous rock with M less than 90, consisting
mainly of alkali feldspar and plagioclase; minor quartz or nepheline
may be present, along with pyroxene, amphibole or biotite. Ratio of
plagioclase to total feldspar is less than 0.65, quartz forms less
than 20 percent of QAPF fraction, and feldspathoid minerals form less
than 10 percent of QAPF fraction. Includes rocks classified in QAPF
fields 6, 7 and 8 and their subdivisions.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Plutonic_Igneous_Rock`
[]{#plutonic_igneous_rock}

Concept: [`Plutonic_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Plutonic_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Instrusive igneous rock formed by crystallisation of magma far enough
below Earth surface that complete crystallization of magma bodies
forms holocrystalline medium to coarse grained igneous rock, wall
rocks generally do not include volcanic products related to the magma,
and some contact metamorphism is tyypically developed at intrusive
contacts.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Porphyry`
[]{#porphyry}

Concept: [`Porphyry`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Porphyry)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock that contains conspicuous phenocrysts in a finer grained
groundmass; groundmass itself may be phaneritic or fine-grained.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Ultrabasic_Igneous_Rock`
[]{#ultrabasic_igneous_rock}

Concept: [`Ultrabasic_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Ultrabasic_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock with less than 45 percent SiO2.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Ultramafic_Igneous_Rock`
[]{#ultramafic_igneous_rock}

Concept: [`Ultramafic_Igneous_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Ultramafic_Igneous_Rock)

Child of:
 [`Igneous_Rock`](#Igneous_Rock)

Igneous rock that consists of greater than 90 percent mafic minerals.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Hornblendite`
[]{#hornblendite}

Concept: [`Hornblendite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Hornblendite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)
 [`Ultramafic_Igneous_Rock`](#Ultramafic_Igneous_Rock)

Ultramafic rock that consists of greater than 40 percent hornblende
plus pyroxene and has a hornblende to pyroxene ratio greater than 1.
Includes olivine hornblendite, olivine-pyroxene hornblendite, pyroxene
hornblendite, and hornblendite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Peridotite`
[]{#peridotite}

Concept: [`Peridotite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Peridotite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)
 [`Ultramafic_Igneous_Rock`](#Ultramafic_Igneous_Rock)

Ultramafic rock consisting of more than 40 percent (by volume) olivine
with pyroxene and/or amphibole and little or no feldspar. commonly
altered to serpentinite. Includes rocks defined modally in the
ultramafic rock classification as dunite, harzburgite, lherzolite,
wehrlite, olivinite, pyroxene peridotite, pyroxene hornblende
peridotite or hornblende peridotite.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroxenite`
[]{#pyroxenite}

Concept: [`Pyroxenite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Pyroxenite)

Child of:
 [`Phaneritic_Igneous_Rock`](#Phaneritic_Igneous_Rock)
 [`Ultramafic_Igneous_Rock`](#Ultramafic_Igneous_Rock)

Ultramafic phaneritic igneous rock composed almost entirely of one or
more pyroxenes and occasionally biotite, hornblende and olivine.
Includes rocks defined modally in the ultramafic rock classification
as olivine pyroxenite, olivine-hornblende pyroxenite, pyroxenite,
orthopyroxenite, clinopyroxenite and websterite.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Impact_Generated_Material`
[]{#impact_generated_material}

Concept: [`Impact_Generated_Material`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Impact_Generated_Material)

Child of:
 [`rock`](#rock)

Material that contains features indicative of shock metamorphism, such
as microscopic planar deformation features within grains or shatter
cones, interpreted to be the result of extraterrestrial bolide impact.
Includes breccias and melt rocks.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Massive_Sulphide`
[]{#massive_sulphide}

Concept: [`Massive_Sulphide`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Massive_Sulphide)

Child of:
 [`rock`](#rock)

rock consisting of greater than 50% sulphide or sulfosalt minerals
formed by any processes. Includes hydrothermal and sedimentary
ehalative sulfide.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Metamorphic_Rock`
[]{#metamorphic_rock}

Concept: [`Metamorphic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Metamorphic_Rock)

Child of:
 [`rock`](#rock)

Robertson (1999, Classification of metamorphic rocks: British
Geological Survey Research Report, RR 99–02) defines the boundary
between diagenesis and metamorphism in sedimentary rocks as follows:
“…the boundary between diagenesis and metamorphism is somewhat
arbitrary and strongly dependent on the lithologies involved. For
example changes take place in organic materials at lower temperatures
than in rocks dominated by silicate minerals. In mudrocks, a white
mica (illite) crystallinity value of less than 0.42 Delta 2 Theta
obtained by X-ray diffraction analysis, is used to define the onset of
metamorphism (Kisch, 1991). In this scheme, the first appearance of
glaucophane, lawsonite, paragonite, prehnite, pumpellyite or
stilpnomelane is taken to indicate the lower limit of metamorphism
(Frey and Kisch, 1987; Bucher and Frey, 1994; Frey and Robinson,
1998). Most workers agree that such mineral growth starts at 150 +/-
50° C in silicate rocks. Many lithologies may show no change in
mineralogy under these conditions and hence the recognition of the
onset of metamorphism will vary with bulk composition.”
Rock formed by solid-state mineralogical, chemical and/or structural
changes to a pre-existing rock, in response to marked changes in
temperature, pressure, shearing stress and chemical environment.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Metasomatic_Rock`
[]{#metasomatic_rock}

Concept: [`Metasomatic_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Metasomatic_Rock)

Child of:
 [`rock`](#rock)

Rock that has fabric and composition indicating open-system
mineralogical and chemical changes in response to interaction with a
fluid phase, typically water rich.
SLTTm (2004) proposed the following criteria to distinguish
hydrothermally altered or metasomatic rock from igneous rock. "The
rock is classified as metamorphic if (1) the texture has been modified
such that it can no longer be considered igneous, (2) the bulk
composition of the rock is inconsistent with compositions that can be
derived purely from a magma and associated processes such as
assimilation and differentiation, or (3) minerals inconsistent with
magmatic crystallization are present."

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Sedimentary_Rock`
[]{#sedimentary_rock}

Concept: [`Sedimentary_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Sedimentary_Rock)

Child of:
 [`rock`](#rock)

Rock formed by accumulation and cementation of solid fragmental
material deposited by air, water or ice, or as a result of other
natural agents, such as precipitation from solution, the accumulation
of organic material, or from biogenic processes, including secretion
by organisms. Includes epiclastic deposits.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Carbonate_Sedimentary_Rock`
[]{#carbonate_sedimentary_rock}

Concept: [`Carbonate_Sedimentary_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Carbonate_Sedimentary_Rock)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Particularly for fine-grained sedimentary rocks, distinction of
'intrabasinal' versus 'clastic' genesis can be very interpretive. In
practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored. Carbonate
rock subcatgories are defined on two orthogonal dimensions--mineralogy
(calcitic vs. dolomitic vs non-carbonate impurities), and texture. The
texture categories used here are those of Dunham (1962), and involve
grain size (matrix vs. grains/allochems), fabric (matrix vs. grain
supported), and genesis (bound, frame, or fragmental). The textural
approach used for carbonate rocks is conceptually incompatible with
that used for clastic sedimentary rocks, which is solely grain size or
mineralogy based. This leads to problems in the vocabulary for rocks
of mixed siliclastic/carbonate mineralogy (grainstone vs. sandstone,
carbonate mudstone vs. carbonate rich mudstone, how to accomodate
marlstone...).
Sedimentary rock in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite, magnesite or dolomite.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Clastic_Sedimentary_Rock`
[]{#clastic_sedimentary_rock}

Concept: [`Clastic_Sedimentary_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Clastic_Sedimentary_Rock)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Sedimentary rock in which at least 50 percent of the constituent
particles were derived from erosion, weathering, or mass-wasting of
pre-existing earth materials, and transported to the place of
deposition by mechanical agents such as water, wind, ice and gravity.
The conglomerate, sandstone, mudstone, and wackestone categories are
not defined as kinds of clastic sedimentary rocks because rocks
meeting their purely grainsize based definitions might also be iron-
rich, phosphatic, or carbonate. This is based on GeoSciML allowance to
assign rocks to more than one lithology category. For example to
categorize a rock as a clastic conglomerate requires assignment ot the
'clastic sedimentary rock' category and to the 'conglomerate'
category. Particularly for fine-grained sedimentary rocks, distinction
of 'intrabasinal' versus 'clastic' genesis can be very interpretive.
In practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Diamictite`
[]{#diamictite}

Concept: [`Diamictite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Diamictite)

Child of:
 [`Clastic_Sedimentary_Rock`](#Clastic_Sedimentary_Rock)

Unsorted or poorly sorted, clastic sedimentary rock with a wide range
of particle sizes including a muddy matrix. Biogenic materials that
have such texture are excluded. Distinguished from conglomerate,
sandstone, mudstone based on polymodality and lack of structures
related to transport and deposition of sediment by moving air or
water. If more than 10 percent of the fine grained matrix is of
indeterminant clastic or diagenetic origin and the fabric is matrix
supported, may also be categorized as wacke.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Generic_Conglomerate`
[]{#generic_conglomerate}

Concept: [`Generic_Conglomerate`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Generic_Conglomerate)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Sedimentary rock composed of at least 30 percent rounded to subangular
fragments larger than 2 mm in diameter; typically contains finer
grained material in interstices between larger fragments. If more than
15 percent of the fine grained matrix is of indeterminant clastic or
diagenetic origin and the fabric is matrix supported, may also be
categorized as wackestone. If rock has unsorted or poorly sorted
texture with a wide range of particle sizes, may also be categorized
as diamictite.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Generic_Mudstone`
[]{#generic_mudstone}

Concept: [`Generic_Mudstone`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Generic_Mudstone)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is so interpretive that it is proposed
to not define the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system. Schnurrenberger, D.,
Russell, J. and Kelts, K., 2003, Classification of lacustrine
sediments based on sedimentary components: Journal of Paleolimnology,
v.29, p141-154.
Sedimentary rock consisting of less than 30 percent gravel-size (2 mm)
particles and with a mud to sand ratio greater than 1. Clasts may be
of any composition or origin.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Generic_Sandstone`
[]{#generic_sandstone}

Concept: [`Generic_Sandstone`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Generic_Sandstone)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Sedimentary rock in which less than 30 percent of particles are
greater than 2 mm in diameter (gravel) and the sand to mud ratio is at
least 1.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Hybrid_Sedimentary_Rock`
[]{#hybrid_sedimentary_rock}

Concept: [`Hybrid_Sedimentary_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Hybrid_Sedimentary_Rock)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Sedimentary rock that does not fit any of the other
composition/genesis categories. Sedimentary rock consisting of three
or more components which form more than 5 percent but less than 50
precent of the material.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Iron_Rich_Sedimentary_Rock`
[]{#iron_rich_sedimentary_rock}

Concept: [`Iron_Rich_Sedimentary_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Iron_Rich_Sedimentary_Rock)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Sedimentary rock that consists of at least 50 percent iron-bearing
minerals (hematite, magnetite, limonite-group, siderite, iron-
sulfides), as determined by hand-lens or petrographic analysis.
Corresponds to a rock typically containing 15 percent iron by weight.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Non_Clastic_Siliceous_Sedimentary_Rock`
[]{#non_clastic_siliceous_sedimentary_rock}

Concept: [`Non_Clastic_Siliceous_Sedimentary_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Non_Clastic_Siliceous_Sedimentary_Rock)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Definition updated to include chert, flint SMR 2020-09-21
Sedimentary rock that consists of at least 50 percent silicate mineral
material, deposited directly by chemical or biological processes at
the depositional surface, in particles formed by chemical or
biological processes within the basin of deposition, or formed by
diagenetic processes. Includes chert and flint found in carbonate
rocks.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Organic_Rich_Sedimentary_Rock`
[]{#organic_rich_sedimentary_rock}

Concept: [`Organic_Rich_Sedimentary_Rock`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Organic_Rich_Sedimentary_Rock)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Sapropelic coal, and asphaltite are not differentiated in This
vocabulary
Sedimentary rock with color, composition, texture and apparent density
indicating greater than 50 percent organic content by weight on a
moisture-free basis.

########  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Coal`
[]{#coal}

Concept: [`Coal`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Coal)

Child of:
 [`Organic_Rich_Sedimentary_Rock`](#Organic_Rich_Sedimentary_Rock)

A consolidated organic sedimentary material having less than 75%
moisture. This category includes low, medium, and high rank coals
according to International Classification of In-Seam Coal (United
Nations, 1998), thus including lignite. Sapropelic coal is not
distinguished in this category from humic coals. Formed from the
compaction or induration of variously altered plant remains similar to
those of peaty deposits.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Phosphorite`
[]{#phosphorite}

Concept: [`Phosphorite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Phosphorite)

Child of:
 [`Sedimentary_Rock`](#Sedimentary_Rock)

Sedimentary rock in which at least 50 percent of the primary or
recrystallized constituents are phosphate minerals. Most commonly
occurs as a bedded primary or reworked secondary marine rock, composed
of microcrystalline carbonate fluorapatite in the form of lamina,
pellets, oolites and nodules, and skeletal, shell and bone fragments.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Tuffite`
[]{#tuffite}

Concept: [`Tuffite`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Tuffite)

Child of:
 [`rock`](#rock)

In practice, it is likely that any rock for which there is suspicion
that it may consist of redeposited pyroclastic material, usually based
on sedimentary structures, irrespective of the presence or percentage
of clearly epiclastic particles, would be called a tuffite. 50 percent
cutoff with epiclastic rock is in contrast with LeMaitre et al., but
is used for consistentency with other sedimentary rock categories
following the pattern that the rock name reflects the predominant
constituent.
Rock consists of more than 50 percent particles of indeterminate
pyroclastic or epiclastic origin and less than 75 percent particles of
clearly pyroclastic origin. commonly the rock is laminated or exhibits
size grading. (based on LeMaitre et al. 2002; Murawski and Meyer
1998).
synonym: volcaniclastic rock

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/residual_material`
[]{#residual_material}

Concept: [`residual_material`](https://w3id.org/isample/vocabulary/rocksediment/0.9/residual_material)

Child of:
 [`rock`](#rock)

Material of composite origin resulting from weathering processes at
the Earth's surface, with genesis dominated by removal of chemical
constituents by aqueous leaching. Minor clastic, chemical, or organic
input may also contribute. Consolidation state is not inherent in
definition, but typically material is unconsolidated or weakly
consolidated.

#####  Sediment

[]{#sediment}

Concept: [`sediment`](https://w3id.org/isample/vocabulary/material/0.9/sediment)

Child of:
 [`rockorsediment`](#rockorsediment)

Solid granular material transported by wind, water, or gravity, not
modified by interaction with biosphere or atmosphere (to differentiate
from soil). Particles derived by erosion of pre-existing rock, from
shell or other body parts from organisms, precipitated chemically in
the surficial environment, or generated by explosive volcanic
activity.
(http://resource.geosciml.org/classifier/cgi/lithology/sediment).
Sediment is not consolidated, i.e. Particulate constituents of a
compound material do not adhere to each other strongly enough that the
aggregate can be considered a solid material in its own right. Similar
to http://purl.obolibrary.org/obo/ENVO_00002007

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Biogenic_Sediment`
[]{#biogenic_sediment}

Concept: [`Biogenic_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Biogenic_Sediment)

Child of:
 [`sediment`](#sediment)

Corresponding biogenic sedimentary material and biogenic sedimentary
rock categories are not included based on the interpretation that
biogenic sedimentary rock will be in a different category, e.g.
carbonate sedimentary rock or organic rich sedimentary rock.
Sediment composed of greater than 50 percent material of biogenic
origin. Because the biogenic material may be skeletal remains that are
not organic, all biogenic sediment is not necessarily organic-rich.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Carbonate_Sediment`
[]{#carbonate_sediment}

Concept: [`Carbonate_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Carbonate_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite and dolomite, in particles of
intrabasinal origin.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Chemical_Sedimentary_Material`
[]{#chemical_sedimentary_material}

Concept: [`Chemical_Sedimentary_Material`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Chemical_Sedimentary_Material)

Child of:
 [`sediment`](#sediment)

Sedimentary material that consists of at least 50 percent material
produced by inorganic chemical processes within the basin of
deposition. Includes inorganic siliceous, carbonate, evaporite, iron-
rich, and phosphatic sediment classes, as well as chemical sediments
associated with submarine hot springs ('black smokers'). Note that
these sediments might crystallize as a solid as they are deposited,
thus similar to rock....

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Clastic_Sediment`
[]{#clastic_sediment}

Concept: [`Clastic_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Clastic_Sediment)

Child of:
 [`sediment`](#sediment)

Choice of 'clastic' is purposful. Other suggested labels for this
category include siliciclastic and terrigineous clastic. Siliciclastic
is considered too limiting because the category includes rocks that
consists clasts of carbonate minerals, e.g. epiclastic detritus eroded
from carbonate rock. Terrigineous clastic was considered and rejected
first because it is considered redundant, anything that is
terrigineous is clastic. Second, it is questionable if clastic
sediment derived by submarine processes (fragementation by gravity
sliding, faulting, or volcanic activity, with transport by sediment
gravity flow or submarine currents) is terrigineous, but it is clastic
and is meant to be included in this category.
Sediment in which at least 50 percent of the constituent particles
were derived from erosion, weathering, or mass-wasting of pre-existing
earth materials, and transported to the place of deposition by
mechanical agents such as water, wind, ice and gravity.

#######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Diamicton`
[]{#diamicton}

Concept: [`Diamicton`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Diamicton)

Child of:
 [`Clastic_Sediment`](#Clastic_Sediment)

Unsorted or poorly sorted, clastic sediment with a wide range of
particle sizes, including a muddy matrix. Biogenic materials that have
such texture are excluded. Distinguished from conglomerate, sandstone,
mudstone based on polymodality and lack of structures related to
transport and deposition of sediment by moving air or water.
Assignment to an other size class can be used in conjunction to
indicate the dominant grain size.
definition amplified to help distinguish diamicton, conglomerate and
wackestone in this version

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Gravel_Size_Sediment`
[]{#gravel_size_sediment}

Concept: [`Gravel_Size_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Gravel_Size_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment containing greater than 30 percent gravel-size particles
(greater than 2.0 mm diameter). Composition or gensis of clasts not
specified.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Hybrid_Sediment`
[]{#hybrid_sediment}

Concept: [`Hybrid_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Hybrid_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment that does not fit any of the other sediment
composition/genesis categories. Sediment consisting of three or more
components which form more than 5 percent but less than 50 precent of
the material.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Iron_Rich_Sediment`
[]{#iron_rich_sediment}

Concept: [`Iron_Rich_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Iron_Rich_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment that consists of at least 50 percent iron-bearing minerals
(hematite, magnetite, limonite-group, siderite, iron-sulfides), as
determined by hand-lens or petrographic analysis. Corresponds to a
rock typically containing 15 percent iron by weight.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Mud_Size_Sediment`
[]{#mud_size_sediment}

Concept: [`Mud_Size_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Mud_Size_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment consisting of less than 30 percent gravel-size (2 mm)
particles and with a mud-size to sand-size particle ratio greater than
1. Clasts may be of any composition or origin.  BGS  (Hallsworth and
Knox, 1999, p. 9) define the  'upper size limit of mud ... at 32
micrometers (.032 mm)', but Wentworth scale and Krumbein scale put
boundary at .064 or .062 mm (inidistinguishable difference in
rocks...) BGS 'mud-grade sediment' or sedimentary rock definition is
'over 75% of the clasts smaller than  .032 mm', which is narrower than
the definition here.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Non_Clastic_Siliceous_Sediment`
[]{#non_clastic_siliceous_sediment}

Concept: [`Non_Clastic_Siliceous_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Non_Clastic_Siliceous_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment that consists of at least 50 percent silicate mineral
material, deposited directly by chemical or biological processes at
the depositional surface, or in particles formed by chemical or
biological processes within the basin of deposition.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Phosphate_Rich_Sediment`
[]{#phosphate_rich_sediment}

Concept: [`Phosphate_Rich_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Phosphate_Rich_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are phosphate minerals.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Sand_Size_Sediment`
[]{#sand_size_sediment}

Concept: [`Sand_Size_Sediment`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Sand_Size_Sediment)

Child of:
 [`sediment`](#sediment)

Sediment in which less than 30 percent of particles are gravel
(greater than 2 mm in diameter) and the sand to mud ratio is at least
1. composition or genesis of clasts not specified.

######  `https://w3id.org/isample/vocabulary/rocksediment/0.9/Tephra`
[]{#tephra}

Concept: [`Tephra`](https://w3id.org/isample/vocabulary/rocksediment/0.9/Tephra)

Child of:
 [`sediment`](#sediment)

Unconsolidated pyroclastic material in which greater than 75 percent
of the fragments are deposited as a direct result of volcanic
processes and the deposit has not been reworked by epiclastic
processes. Includes ash, lapilli tephra, bomb tephra, block tephra and
unconsolidated agglomerate.

####  Soil

[]{#soil}

Concept: [`soil`](https://w3id.org/isample/vocabulary/material/0.9/soil)

Child of:
 [`earthmaterial`](#earthmaterial)

Mixed granular mineral and organic matter modified by interaction
between earth material, biosphere, and atmosphere, consisting mostly
of varying proportions of sand, silt, and clay, organic material such
as humus, gases, liquids, and a broad range of resident micro- and
macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of
horizons near the Earth's surface that, in contrast to the underlying
parent material, have been altered by the interactions of climate,
relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/
portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
(http://purl.obolibrary.org/obo/ENVO_00001998)

See Also:

* [<http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280>](http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)

###  Fluid material

[]{#fluid}

Concept: [`fluid`](https://w3id.org/isample/vocabulary/material/0.9/fluid)

Child of:
 [`material`](#material)

a substance that continually deforms (flows) under an applied shear
stress, or external force. Fluids are a phase of matter and include
liquids, gases and plasmas. They are substances with zero shear
modulus, or, in simpler terms, substances that cannot resist any shear
force applied to them. (https://en.wikipedia.org/wiki/Fluid)

####  Gaseous material

[]{#gas}

Concept: [`gas`](https://w3id.org/isample/vocabulary/material/0.9/gas)

Child of:
 [`fluid`](#fluid)

Material composed of one or more chemical entities that has neither
independent shape nor volume but tends to expand indefinitely
(http://purl.obolibrary.org/obo/ENVO_01000797). Infer that the sample
is curated in some kind of container.

####  Liquid water

[]{#liquidwater}

Concept: [`liquidwater`](https://w3id.org/isample/vocabulary/material/0.9/liquidwater)

Child of:
 [`fluid`](#fluid)

A material primarily composed of dihydrogen oxide in its liquid form;
infer that the sample is curated in some kind of container.

####  Non-aqueous liquid material

[]{#nonaqueousliquid}

Concept: [`nonaqueousliquid`](https://w3id.org/isample/vocabulary/material/0.9/nonaqueousliquid)

Child of:
 [`fluid`](#fluid)

Liquid composed dominantly of material other than water. Includes
liquids that do not fit in any other category. E.g. alcohol,
petroleum.

###  Organic material

[]{#organicmaterial}

Concept: [`organicmaterial`](https://w3id.org/isample/vocabulary/material/0.9/organicmaterial)

Child of:
 [`material`](#material)

Environmental material derived from living organisms and composed
primarily of one or more very large molecules of biological origin.
Examples: body (animal or plant), body part, fecal matter, seeds,
wood, tissue, biological fluids, biological waste, algal material,
biofilm, necromass, plankton. source:
http://purl.obolibrary.org/obo/ENVO_01000155

####  Anthropogenic organic material

[]{#anthropogenicorganicmaterial}

Concept: [`anthropogenicorganicmaterial`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/anthropogenicorganicmaterial)

Child of:
 [`organicmaterial`](#organicmaterial)
 [`otheranthropogenicmaterial`](#otheranthropogenicmaterial)

Organic material manufactured by humans

#####  Plastic (material)

[]{#plastic}

Concept: [`plastic`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/plastic)

Child of:
 [`anthropogenicorganicmaterial`](#anthropogenicorganicmaterial)

Synthetic or semi-synthetic material that uses organic polymers as a
main ingredient.

See Also:

* [""]()

####  Organic animal product

[]{#organicanimalproduct}

Concept: [`organicanimalproduct`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/organicanimalproduct)

Child of:
 [`organicmaterial`](#organicmaterial)


#####  Hair

[]{#hair}

Concept: [`hair`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/hair)

Child of:
 [`organicanimalproduct`](#organicanimalproduct)


#####  Leather

[]{#leather}

Concept: [`leather`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/leather)

Child of:
 [`organicanimalproduct`](#organicanimalproduct)


####  Organic animal material

[]{#organicanimalmaterial}

Concept: [`organicanimalmaterial`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/organicanimalmaterial)

Child of:
 [`organicmaterial`](#organicmaterial)


####  Organic plant material

[]{#organicplantmaterial}

Concept: [`organicplantmaterial`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/organicplantmaterial)

Child of:
 [`organicmaterial`](#organicmaterial)


#####  Wood

[]{#wood}

Concept: [`wood`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/wood)

Child of:
 [`plantmaterial`](#plantmaterial)
 [`organicplantmaterial`](#organicplantmaterial)


####  Plant Material

[]{#plantmaterial}

Concept: [`plantmaterial`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/plantmaterial)

Child of:
 [`organicmaterial`](#organicmaterial)


#####  Plant fiber

[]{#plantfiber}

Concept: [`plantfiber`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/plantfiber)

Child of:
 [`plantmaterial`](#plantmaterial)


#####  Wood

[]{#wood}

Concept: [`wood`](https://w3id.org/isample/vocabulary/opencontext/material/0.1/wood)

Child of:
 [`plantmaterial`](#plantmaterial)
 [`organicplantmaterial`](#organicplantmaterial)



