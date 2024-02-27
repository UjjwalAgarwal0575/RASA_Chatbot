package com.example.esquery.service;

import java.io.IOException;
import java.util.function.Supplier;

import co.elastic.clients.elasticsearch._types.query_dsl.Query;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.esquery.model.product;
import com.example.esquery.util.elasticSearchUtil;

import co.elastic.clients.elasticsearch.ElasticsearchClient;
import co.elastic.clients.elasticsearch.core.SearchResponse;

@Service
public class elasticSearchService {

    @Autowired
    private ElasticsearchClient elasticsearchClient;

    public SearchResponse<product> fuzzySearch(String approximateProductName) throws IOException {
        Supplier<Query>  supplier = elasticSearchUtil.createSupplierQuery(approximateProductName);
       SearchResponse<product> response = elasticsearchClient.search(s->s.index("product").query(supplier.get()),product.class);
        System.out.println("elasticsearch supplier fuzzy query "+supplier.get().toString());
        return response;
    }
}