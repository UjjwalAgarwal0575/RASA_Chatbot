package com.example.esquery.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.esquery.model.product;
import com.example.esquery.repository.productRepository;

@Service

public class productService {

    @Autowired
    private productRepository productRepo;

    public Iterable<product> getProducts() {
     return productRepo.findAll();
    }

    public product insertProduct(product product) {
        return productRepo.save(product);
    }

    public product updateProduct(product product, int id) {
        product product1  = productRepo.findById(id).get();
        product1.setPrice(product.getPrice());
        return product1;
    }

    public void deleteProduct(int id ) {
        productRepo.deleteById(id);
    }

}