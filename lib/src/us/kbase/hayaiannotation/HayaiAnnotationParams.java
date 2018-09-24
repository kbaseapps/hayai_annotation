
package us.kbase.hayaiannotation;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: HayaiAnnotationParams</p>
 * <pre>
 * Here we define the parameters that are passed from the UI
 * The same parameters need to be defined in ui/narrative/methods/
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "input_ws",
    "input_genome",
    "output_genome",
    "alignment_type",
    "organism_type",
    "max_hits_per_query",
    "max_seq_id",
    "max_e_value",
    "query_coverage",
    "target_coverage"
})
public class HayaiAnnotationParams {

    @JsonProperty("input_ws")
    private String inputWs;
    @JsonProperty("input_genome")
    private String inputGenome;
    @JsonProperty("output_genome")
    private String outputGenome;
    @JsonProperty("alignment_type")
    private String alignmentType;
    @JsonProperty("organism_type")
    private String organismType;
    @JsonProperty("max_hits_per_query")
    private Long maxHitsPerQuery;
    @JsonProperty("max_seq_id")
    private Double maxSeqId;
    @JsonProperty("max_e_value")
    private Double maxEValue;
    @JsonProperty("query_coverage")
    private Double queryCoverage;
    @JsonProperty("target_coverage")
    private Double targetCoverage;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("input_ws")
    public String getInputWs() {
        return inputWs;
    }

    @JsonProperty("input_ws")
    public void setInputWs(String inputWs) {
        this.inputWs = inputWs;
    }

    public HayaiAnnotationParams withInputWs(String inputWs) {
        this.inputWs = inputWs;
        return this;
    }

    @JsonProperty("input_genome")
    public String getInputGenome() {
        return inputGenome;
    }

    @JsonProperty("input_genome")
    public void setInputGenome(String inputGenome) {
        this.inputGenome = inputGenome;
    }

    public HayaiAnnotationParams withInputGenome(String inputGenome) {
        this.inputGenome = inputGenome;
        return this;
    }

    @JsonProperty("output_genome")
    public String getOutputGenome() {
        return outputGenome;
    }

    @JsonProperty("output_genome")
    public void setOutputGenome(String outputGenome) {
        this.outputGenome = outputGenome;
    }

    public HayaiAnnotationParams withOutputGenome(String outputGenome) {
        this.outputGenome = outputGenome;
        return this;
    }

    @JsonProperty("alignment_type")
    public String getAlignmentType() {
        return alignmentType;
    }

    @JsonProperty("alignment_type")
    public void setAlignmentType(String alignmentType) {
        this.alignmentType = alignmentType;
    }

    public HayaiAnnotationParams withAlignmentType(String alignmentType) {
        this.alignmentType = alignmentType;
        return this;
    }

    @JsonProperty("organism_type")
    public String getOrganismType() {
        return organismType;
    }

    @JsonProperty("organism_type")
    public void setOrganismType(String organismType) {
        this.organismType = organismType;
    }

    public HayaiAnnotationParams withOrganismType(String organismType) {
        this.organismType = organismType;
        return this;
    }

    @JsonProperty("max_hits_per_query")
    public Long getMaxHitsPerQuery() {
        return maxHitsPerQuery;
    }

    @JsonProperty("max_hits_per_query")
    public void setMaxHitsPerQuery(Long maxHitsPerQuery) {
        this.maxHitsPerQuery = maxHitsPerQuery;
    }

    public HayaiAnnotationParams withMaxHitsPerQuery(Long maxHitsPerQuery) {
        this.maxHitsPerQuery = maxHitsPerQuery;
        return this;
    }

    @JsonProperty("max_seq_id")
    public Double getMaxSeqId() {
        return maxSeqId;
    }

    @JsonProperty("max_seq_id")
    public void setMaxSeqId(Double maxSeqId) {
        this.maxSeqId = maxSeqId;
    }

    public HayaiAnnotationParams withMaxSeqId(Double maxSeqId) {
        this.maxSeqId = maxSeqId;
        return this;
    }

    @JsonProperty("max_e_value")
    public Double getMaxEValue() {
        return maxEValue;
    }

    @JsonProperty("max_e_value")
    public void setMaxEValue(Double maxEValue) {
        this.maxEValue = maxEValue;
    }

    public HayaiAnnotationParams withMaxEValue(Double maxEValue) {
        this.maxEValue = maxEValue;
        return this;
    }

    @JsonProperty("query_coverage")
    public Double getQueryCoverage() {
        return queryCoverage;
    }

    @JsonProperty("query_coverage")
    public void setQueryCoverage(Double queryCoverage) {
        this.queryCoverage = queryCoverage;
    }

    public HayaiAnnotationParams withQueryCoverage(Double queryCoverage) {
        this.queryCoverage = queryCoverage;
        return this;
    }

    @JsonProperty("target_coverage")
    public Double getTargetCoverage() {
        return targetCoverage;
    }

    @JsonProperty("target_coverage")
    public void setTargetCoverage(Double targetCoverage) {
        this.targetCoverage = targetCoverage;
    }

    public HayaiAnnotationParams withTargetCoverage(Double targetCoverage) {
        this.targetCoverage = targetCoverage;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((((((((((((("HayaiAnnotationParams"+" [inputWs=")+ inputWs)+", inputGenome=")+ inputGenome)+", outputGenome=")+ outputGenome)+", alignmentType=")+ alignmentType)+", organismType=")+ organismType)+", maxHitsPerQuery=")+ maxHitsPerQuery)+", maxSeqId=")+ maxSeqId)+", maxEValue=")+ maxEValue)+", queryCoverage=")+ queryCoverage)+", targetCoverage=")+ targetCoverage)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
