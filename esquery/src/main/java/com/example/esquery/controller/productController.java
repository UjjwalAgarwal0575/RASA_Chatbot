package com.example.esquery.controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.esquery.model.product;
import com.example.esquery.service.elasticSearchService;
import com.example.esquery.service.productService;

import co.elastic.clients.elasticsearch.core.SearchResponse;
import co.elastic.clients.elasticsearch.core.search.Hit;

@RestController
@RequestMapping("/apis")
public class productController {
     @Autowired
    private productService productService;

    @Autowired
    private elasticSearchService elasticSearchService;

    @GetMapping("/findAll")
    Iterable<product> findAll(){
       return productService.getProducts();
    }

    @PostMapping("/insert")
    public product insertProduct(@RequestBody  product product){
       return productService.insertProduct(product);
    }

    @GetMapping("/fuzzySearch/{approximateProductName}")
    List<product> fuzzySearch( @PathVariable String approximateProductName ) throws IOException {
        SearchResponse<product> searchResponse = elasticSearchService.fuzzySearch(approximateProductName);
       List<Hit<product>> hitList = searchResponse.hits().hits();
        System.out.println(hitList);
        List<product> productList = new ArrayList<>();
        for(Hit<product> hit :hitList){
            productList.add(hit.source());
        }
        return productList;
    }
}
