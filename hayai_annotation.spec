/*
A KBase module: hayai_annotation
*/

module hayai_annotation {
    /*
        Here we define the parameters that are passed from the UI
	The same parameters need to be defined in ui/narrative/methods/
    */

   typedef structure {

       string input_ws;
       string input_genome;
       string output_genome;
       string alignment_type;
       string organism_type;
       int max_hits_per_query;
       float max_seq_id;
       float max_e_value;
       float query_coverage;
       float target_coverage;

   } AnnotatePlantGenomeParams;

   /*
       Here we define the output, which, for the purposes of the UI, will always be a report.
       The contents of the report are shown, in HTML, in the output widget.
   */
    typedef structure {
        string report_name;
        string report_ref;
    } AnnotatePlantGenomeResults;

    /*
        Here we define an actual function.
    */
    funcdef annotate_plant_genome(AnnotatePlantGenomeParams input) returns (AnnotatePlantGenomeResults output) authentication required;

};
