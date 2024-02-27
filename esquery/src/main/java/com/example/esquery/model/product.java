package com.example.esquery.model;

import org.springframework.data.elasticsearch.annotations.Document;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


@AllArgsConstructor
@NoArgsConstructor
@Data
@Document(indexName = "product")
@JsonIgnoreProperties(ignoreUnknown = true)
public class product {
    private String _id;
    private String _index;
    private int _score;
    private String _type;
    private String availability;
    private String brand;
    private String condition;
    private String description;
    private int id;
    private String image_link;
    private String item_group_id;
    private String link;
    private String origin_country;
    private int price;
    private int quantity_to_sell_on_facebook;
    private String title;
}
