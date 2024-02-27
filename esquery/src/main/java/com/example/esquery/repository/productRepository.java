package com.example.esquery.repository;

import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import com.example.esquery.model.product;

public interface productRepository extends ElasticsearchRepository<product,Integer>{
    
}
